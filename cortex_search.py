import snowflake.connector
from dotenv import load_dotenv
import os

load_dotenv()

def query_cortex_search(query):
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT")
    )
    cursor = conn.cursor()
    sql = f"SELECT content FROM DOCUMENTS WHERE MATCH(content, '{query}')"
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    return results
