from db_do import get_db_connection

def get_data_from_db(table,needed_column,column,row):
    conn = get_db_connection()

    cur = conn.cursor()

    cur.execute(f"SELECT {needed_column} FROM {table} WHERE {column} = '{row}';")
    res = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

    return res

def insert_data_by_name(table, needed_column, newvalue_to_column, pointer_value, pointer):
    conn = get_db_connection()

    cur = conn.cursor()

    cur.execute(f"UPDATE {table} SET {needed_column} = '{newvalue_to_column}' WHERE {pointer} = '{pointer_value}';")

    conn.commit()
    cur.close()
    conn.close()

# insert_data_by_name('clients','pass','e45d90957eec7387726c6a1b174da7b566a24ff4cb060dcbcdfebb931a93ffe3','anna','name')

def insert_code(table,column,value):
    conn = get_db_connection()

    cur = conn.cursor()

    cur.execute(f"INSERT INTO {table} ({column}) VALUES ('{value}');")

    conn.commit()
    cur.close()
    conn.close()
    