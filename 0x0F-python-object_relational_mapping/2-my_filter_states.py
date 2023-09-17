#!/usr/bin/python3
"""  tables matching the information will be returned """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor_create = db.cursor()
    cursor_create.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows_check = cursor_create.fetchall()
    for row in rows_check:
        print(row)
    cursor_create.close()
    db.close()
