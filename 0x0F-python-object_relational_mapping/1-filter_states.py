#!/usr/bin/python3
"""list all states in the database."""
import sys
import MySQLdb

if __name__ == "__main__":
    # information from database will be received 
    # connection to MYSQL database
    database_connect = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], database_connect=sys.argv[3])
    credentials = database_connect.cursor()

    #execution of the mysql query
    credentials.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in credentials.fetchall() if state[1][0] == "N"]


