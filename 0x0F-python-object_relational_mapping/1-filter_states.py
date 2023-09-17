#!/usr/bin/python3
"""Returns the information from the database."""
import sys
import MySQLdb

if __name__ == "__main__":
    # connection to the database
    database_create = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], database_create=sys.argv[3])
    cursor_run = database_create.cursor()

    # execute the query in order
    cursor_run.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]

