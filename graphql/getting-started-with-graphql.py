#!/usr/bin/env python

import json
from graphene import ObjectType, String, Schema, List, Field
from time import time as timer
from collections import namedtuple


ValueTypeAttribute = namedtuple('ValueTypeAttribute', ['key', 'value'])
ValueTypeEntity = namedtuple('ValueTypeEntity', ['entity_id', 'attributes'])


ATTRIBUTES = {
    "1": [
        ValueTypeAttribute("knows", "2")
    ],
    "2": [
        ValueTypeAttribute("knows", "1")
    ]
}

ENTITIES = [
    ValueTypeEntity(x, [])
    for x in ATTRIBUTES.keys()
]

class Attribute(ObjectType):
    key = String()
    value = String()

class Entity(ObjectType):
    entity_id = String()
    attributes = List(Attribute, keys=List(String))

    def resolve_attributes(entity, info, keys=None):
        attributes = ATTRIBUTES.get(entity.entity_id, [])
        attr_filter = lambda x: x.key in keys if keys else False
        return [Attribute(x.key, x.value) for x in attributes if attr_filter(x)]

class Query(ObjectType):
    all = List(Entity)
    latest = Field(Entity)
    test = String(returns=String())

    def resolve_all(root, info):
        return [Entity(e.entity_id) for e in ENTITIES]
    
    def resolve_latest(root, info):
        return Entity(ENTITIES[-1].entity_id)
    
    def resolve_test(root, info, returns):
        return returns


queries = [
# ----------------
"""
{
    all
    latest
    test(returns:  "hi")
}
""",
# ----------------
'{ test(returns:  "hi") }',
# ----------------
"""
{ 
    latest { 
        entityId, 
        attributes(keys: ["knows"]) {
            key,
            value
        } 
    } 
}
""",
# ----------------
'{ latest { entityId } }',
# ----------------
'{ all { entityId } }',
# ----------------
'''
{ 
    all { 
        entityId, 
        attributes(keys: []) {
            key, 
            value
        }
    } 
}'''
# ----------------
]

# def timing_middleware(next, root, info, **args):
#     start = timer()
#     return_value = next(root, info, **args)
#     duration = round((timer() - start) * 1000, 2)
#     parent_type_name = root._meta.name if root and hasattr(root, '_meta') else ''
#     print(f"{parent_type_name}.{info.field_name}: {duration} ms")
#     return return_value


schema = Schema(query=Query)
print(schema)
print("-"*50)
for query_string in queries:
    result = schema.execute(query_string)
    # result = schema.execute(query_string, middleware=[timing_middleware])
    print(query_string)
    print(json.dumps(result.data, indent=4))
    print("-"*50)
