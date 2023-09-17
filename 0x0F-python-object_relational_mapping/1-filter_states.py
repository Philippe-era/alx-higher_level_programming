#!/usr/bin/python3
"""all information from database will be returned """
""" returns information on database based on conditions set """
import MySQLdb
import sys


if __name__ == "__main__":
    database_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database_connect=sys.argv[3], port=3306)
    cursor_create = database_connect.cursor()
    cursor_create.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows_check = cursor_create.fetchall()
    for row in rows_check:
        print(row)
    cursor_create.close()
    database_connect.close()
