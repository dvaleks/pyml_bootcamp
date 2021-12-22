'''
Задание:
Используя sqlite3, напишите код, который создает таблицу базы данных
для датасета с CityId городов различных стран мира, приведенного в файле

https://worldweather.wmo.int/en/json/full_city_list.txt. Предусмотреть функ-
цию, позволяющую вносить изменения в базу данных. Продемонстрировать

её работу.
'''

import sqlite3
import sys


def cursor_exec(connection: sqlite3.Connection, cursor: sqlite3.Cursor,
                sql: str, row: tuple = None, commit: bool = True):
    try:
        if row:
            cursor.execute(sql, row)
        else:
            cursor.execute(sql)
        if commit:
            connection.commit()
    except sqlite3.DatabaseError as ex:
        print('Oops! Exception: {0}'.format(ex))
        cursor.close()
        connection.close()
        exit(1)


def main():
    action = 'write'
    if len(sys.argv) > 1:
        action = sys.argv[1]
    if action not in ('write', 'read_all', 'read_where', 'execute'):
        print('Unsupported action: {0}'.format(action))
        exit(1)
    if action in ('execute', 'where') and len(sys.argv) < 3:
        print('SQL statement not provided!')
        exit(1)

    con = sqlite3.connect('city_id.db')
    cursor = con.cursor()

    if action == 'write':
        do_write(con, cursor)
    elif action == 'read_all':
        data = do_read(con, cursor)
        print(data)
        print('len:', len(data))
    elif action == 'read_where':
        sql = sys.argv[2]
        data = do_read(con, cursor, sql)
        print(data)
        print('len:', len(data))
    elif action == 'execute':
        sql = sys.argv[2]
        cursor_exec(con, cursor, sql)

    cursor.close()
    con.close()
    print('done action:', action)


def do_write(con, cursor):
    sql = '''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_id INTEGER,
            country VARCHAR(255),
            city VARCHAR(255),
            UNIQUE(city_id)
        );
    '''
    cursor_exec(con, cursor, sql)

    sql = '''
        INSERT OR IGNORE INTO cities (country, city, city_id) VALUES (?, ?, ?)
    '''
    with open('city_id.csv', 'r') as file:
        for line in file:
            row = tuple(line.replace('\n', '').replace('"', '').split(';'))
            cursor_exec(con, cursor, sql, row)


def do_read(con, cursor, where=None):
    if where:
        cursor.execute('SELECT * FROM cities WHERE ' + where)
    else:
        cursor.execute('SELECT * FROM cities')
    return cursor.fetchall()


if __name__ == '__main__':
    main()
