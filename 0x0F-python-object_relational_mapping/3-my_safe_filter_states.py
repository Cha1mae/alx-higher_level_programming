#!/usr/bin/python3
"""
takes in args and displaays all the values in states
the name matches the args and its safe from sql
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cr = db.cursor()
    cr.execute("""SELECT * FROM states WHERE BINARY name = %s
                    ORDER BY id""", (name,))
    rows = cr.fetchall()
    for row in rows:
        print(row)

    cr.close()
    db.close()
