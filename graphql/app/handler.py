#!/usr/bin/env python

# ------------------------------------------------------------------------------

# Setting the Defaul Query! ...
# https://stackoverflow.com/questions/3536620/how-to-change-a-module-variable-from-another-module
# https://github.com/encode/starlette/blob/master/starlette/graphql.py#L266
# https://stackoverflow.com/questions/5626193/what-is-monkey-patching

# TODO: Turn this monkey patch into a PR.

def escape_multiline_string(s: str) -> str:
    return s.strip().replace("\n", "\\n").replace("    ", "\\t")

import starlette.graphql
query = escape_multiline_string("""

# { 
#     all { 
#         entityId, 
#         attributes(keys: []) { 
#             key, 
#             value 
#         } 
#     } 
# }

# https://graphql.org/learn/queries/#fragments

mutation runMutation($entites: [InputEntity]!) {
    updateEntities(entities: $entites ) {
        ok
        updatedEntities {
            entityId
            attributes {
                attributeId
                key
                value
            }
        }
    }
}
""")
variables = escape_multiline_string("""
{
    "entites": [ 
        { 
            "entityId":"e3", 
            "attributes": [ 
                { 
                    "key": "knows", 
                    "value": "{\\\\"entity\\\\": \\\\"e1\\\\"}" 
                } 
            ] 
        } 
    ]
}
""")
starlette.graphql.GRAPHIQL = starlette.graphql.GRAPHIQL.replace(
    "query: parameters.query,", 
    f"query: parameters.query,\n\t  defaultQuery: '{query}',"
)
starlette.graphql.GRAPHIQL = starlette.graphql.GRAPHIQL.replace(
    "variables: parameters.variables", 
    f"variables: '{variables}'"
)
print(starlette.graphql.GRAPHIQL)
# ------------------------------------------------------------------------------
from typing import List, Dict
import psycopg2
from psycopg2.extras import Json
import datetime
import pydash
import json
import graphene
import pandas.io.sql as sqlio
from fastapi import FastAPI

app = FastAPI()

# https://www.postgresqltutorial.com/postgresql-python/insert/
# https://www.psycopg.org/docs/usage.html#python-types-adaptation
# https://www.postgresqltutorial.com/postgresql-python/transaction/

def increment_ingestion(conn_factory, table="app.jobs", column_names="job_type,job_started,job_ended,files,file_records", id_column="job_id"):
    ingestion_id = None
    placeholders = ",".join(["%s"]*len(column_names.split(",")))
    sql = f"INSERT INTO {table}({column_names}) VALUES({placeholders}) RETURNING {id_column}"
    try:
        print(f"executing {sql}")
        conn = conn_factory()
        # create a new cursor
        cur = conn.cursor()
        
        # # http://zetcode.com/python/psycopg2/
        # expanded_query = cur.mogrify(sql, ("ingestion", datetime.datetime.utcnow(), datetime.datetime.utcnow(), ["api"], [0]))
        # print(f"Running: {expanded_query}")
        
        # execute the INSERT statement
        cur.execute(sql, ("ingestion", datetime.datetime.utcnow(), datetime.datetime.utcnow(), ["api"], [0]))
        # get the generated id back
        ingestion_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error Occured: {error}")
        if conn:
            conn.rollback()
    finally:
        # close communication with the database
        if cur:
            cur.close()
    return ingestion_id



def insert_items(conn_factory, table, columns, items: List[Dict]):
    placeholders = ",".join(["%s"]*len(columns))
    column_names = ",".join(columns)
    sql = f"INSERT INTO {table}({column_names}) VALUES({placeholders})"
    try:
        conn = conn_factory()
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(
            sql,
            [
                tuple([x.get(k) for k in columns]) 
                for x in items
            ]
        )
        # commit the changes to the database
        conn.commit()
        
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    

def get_grapql_app(conn):

    class Attribute(graphene.ObjectType):
        attribute_id = graphene.String()
        key = graphene.String()
        value = graphene.String()


    class Entity(graphene.ObjectType):
        entity_id = graphene.String()
        attributes = graphene.List(Attribute, keys=graphene.List(graphene.String))

        def resolve_attributes(entity, info, keys=None):
            sql = f"""
                SELECT * from app.attributes where entity_id = '{entity["entity_id"]}' ; 
            """
            df = sqlio.read_sql_query(sql, conn())
            print(df)
            return df.to_dict(orient="records")


    class InputAttribute(graphene.InputObjectType):
        key = graphene.String()
        value = graphene.String()


    class InputEntity(graphene.InputObjectType):
        entity_id = graphene.String()
        attributes = graphene.List(InputAttribute)


    class MutateEntities(graphene.Mutation):
        class Arguments:
            entities = graphene.List(InputEntity)

        ok = graphene.Boolean()
        updated_entities = graphene.List(Entity)

        def mutate(root, info, entities):
            ingestion_id = increment_ingestion(conn)
            columns = ["ingestion_id", "entity_id", "key", "value"]
            updated_attributes = [
                dict(zip(
                    columns,
                    [
                        ingestion_id,
                        e.entity_id,
                        a.key,
                        # https://stackoverflow.com/questions/31796332/psycopg2-insert-python-dictionary-as-json/31796487
                        Json(json.loads(a.value))
                    ]
                ))
                for e in entities
                for a in e.attributes
            ]
            print(updated_attributes)
            insert_items(conn, "app.attributes", columns, updated_attributes)
            ok = True
            return MutateEntities(
                updated_entities=Queries.resolve_all_in_ingestion(root, info, ingestion_id), 
                ok=ok
            )


    class Queries(graphene.ObjectType):
        all = graphene.List(Entity)
        all_in_ingestion = graphene.List(Entity, ingestion_id=graphene.Int())
        latest = graphene.Field(Entity)
        test = graphene.String(returns=graphene.String())

        @staticmethod
        def resolve_all(root, info):
            sql = f"SELECT DISTINCT entity_id from app.attributes;"
            df = sqlio.read_sql_query(sql, conn())
            return df.to_dict(orient="records")
        
        @staticmethod
        def resolve_all_in_ingestion(root, info, ingestion_id):
            sql = f"SELECT DISTINCT entity_id from app.attributes where ingestion_id = {ingestion_id};"
            df = sqlio.read_sql_query(sql, conn())
            return df.to_dict(orient="records")


    class Mutations(graphene.ObjectType):
        # update_entities = graphene.Field(MutateEntities)
        update_entities = MutateEntities.Field()

    gql_app = starlette.graphql.GraphQLApp(schema=graphene.Schema(query=Queries, mutation=Mutations))

    return gql_app
