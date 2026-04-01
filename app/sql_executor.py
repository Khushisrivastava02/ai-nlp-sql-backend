import sqlite3

def execute_sql(query):
    # Only allow SELECT queries
    if not query.lower().startswith("select"):
        return {"error": "Only SELECT queries are allowed"}

    conn = sqlite3.connect("edtech.db")
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception as e:
        result = str(e)

    conn.close()

    return result