
from fastapi import FastAPI

app = FastAPI()

import psycopg2
import pandas as pd
import pandas.io.sql as sqlio
from handler import get_grapql_app

conn = None
conn_factory = lambda: conn


@app.on_event("startup")
def startup_event():
    # print("startup event")
    global conn
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="password"
    )


@app.on_event("shutdown")
def shutdown_event():
    # print("shutdown event")
    if conn:
      conn.close()


@app.get("/test")
def handler():
    sql = "SELECT * from app.attributes;"
    df = sqlio.read_sql_query(sql, conn)
    # print(df.to_markdown(index=False))
    return df.to_dict(orient="records")


app.add_route("/", get_grapql_app(conn_factory))