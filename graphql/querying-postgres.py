#!/usr/bin/env python 

# https://www.postgresqltutorial.com/postgresql-python/connect/
# https://gist.github.com/jakebrinkmann/de7fd185efe9a1f459946cf72def057e
# https://www.tutlinks.com/fastapi-with-postgresql-crud-async/

import psycopg2
import pandas as pd
import pandas.io.sql as sqlio

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="password"
)

sql = "SELECT * from app.attributes;"
df = sqlio.read_sql_query(sql, conn)
print(df.to_markdown(index=False))