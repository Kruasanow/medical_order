from db_do import get_db_connection

def get_data_from_db(table,needed_column,column,row):
    conn = get_db_connection()

    cur = conn.cursor()

    cur.execute(f"SELECT {needed_column} FROM {table} WHERE {column} = '{row}';")
    res = cur.fetchall()

    return res

