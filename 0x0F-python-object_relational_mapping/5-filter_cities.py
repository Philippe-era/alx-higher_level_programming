#!/usr/bin/python3
"""  lists information from the databse """
""" seperation by citites """
import MySQLdb
import sys


if __name__ == "__main__":
    database_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor_create = database_connect.cursor()
    cursor_create.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows_check = cursor_create.fetchall()
    temporary_data = list(row[0] for row in rows_check)
    print(*temporary_data, sep=", ")
    cursor_create.close()
    database_connect.close()
