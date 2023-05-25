from db_do import get_db_connection
def check_n_insert():
    # Значения, которые нужно вставить
    value1 = 'anna'
    value2 = 'e45d90957eec7387726c6a1b174da7b566a24ff4cb060dcbcdfebb931a93ffe3' # Захэшированный passw
    conn = get_db_connection()
    cur = conn.cursor()
    # Проверка наличия записей с такими значениями
    cur.execute('''SELECT * FROM clients WHERE name=%s AND pass=%s''', (value1, value2))
    existing_rows = cur.fetchall()

    if len(existing_rows) == 0:
        # Вставка значений в таблицу
        cur.execute('''INSERT INTO clients (name,pass) VALUES (%s, %s)''', (value1, value2))
        conn.commit()
        print('Значения успешно вставлены.')
    else:
        print('Значения уже существуют и не будут вставлены.')
