#!/usr/bin/python3
"""All states of the united states will be displayed"""
import sys
import MySQLdb

def list_states (username, password, database):
    """all states will be displayed in the database created
    Ags:
        username: mysql username
        password: mysql password
        database: mysql database
    """
    # This line of code connects to the MYSQL DATABASE
    database_connect = MySQLdb.connect(host='localhost',\
            port=3306,\
            user=username,\
            passwd=password,\
            database_connect=database)
    cursor = database_connect.cursor()

    # Query to be executed
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

   
    rows_display = cursor.fetchall()

    # ALL DATA TO BE PRINTED
    for initial in rows_display:
        print(intial)

    # Close the database connection
    Database_connect.close()

# Example usage
if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)


