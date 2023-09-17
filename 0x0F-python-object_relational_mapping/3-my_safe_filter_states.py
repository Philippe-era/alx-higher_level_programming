#!/usr/bin/python3
"""  SQL injections  """
""" filtering the states (province) """
import MySQLdb
import sys


if __name__ == "__main__":
    database_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database_connect=sys.argv[3], port=3306)
    cursor_create = database_connect.cursor()
    match_conditions = sys.argv[4]
    cursor_create.execute("SELECT * FROM states WHERE name LIKE %s", (match_conditions, ))
    rows_check = cursor_create.fetchall()
    for row in rows_check:
        print(row)
    cursor_create.close()
    database_connect.close()
