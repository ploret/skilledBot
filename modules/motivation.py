import sqlite3


def get_random_quotation(sqlite_file, sqlite_table):
    connect = sqlite3.connect(sqlite_file)
    cursor = connect.cursor()
    cursor.execute("SELECT quotation, author FROM %s ORDER BY RANDOM() LIMIT 1" % sqlite_table)
    row = cursor.fetchone()
    cursor.close()
    quotation_info = {
        'text': row[0],
        'author': row[1]
    }
    return quotation_info
