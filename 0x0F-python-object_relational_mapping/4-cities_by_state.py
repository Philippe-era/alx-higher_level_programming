#!/usr/bin/python3
""" information from the database """
""" cities in the database executed """
import MySQLdb
import sys


if __name__ == "__main__":
    database_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor_connect = database_connect.cursor()
    cursor_create.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows_check = cursor_create.fetchall()
    for row in rows_check:
        print(row)
    cursor_create.close()
    database_connect.close()
