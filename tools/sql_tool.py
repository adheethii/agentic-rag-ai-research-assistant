import sqlite3
import pandas as pd

def query_database(query):

    conn = sqlite3.connect("data/database/data.db")

    df = pd.read_sql(query, conn)

    conn.close()

    return df