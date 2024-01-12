#!/usr/bin/python3
"""
takes an arg that displays all the valieus from the data base
where the name matches the arg
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
    cr.execute("""SELECT * FROM states WHERE BINARY name = '{}'
                    ORDER BY id""".format(name))

    rows = cr.fetchall()
    for row in rows:
        print(row)
    cr.close()
    db.close()
