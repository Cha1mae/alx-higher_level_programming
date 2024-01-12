#!/usr/bin/python3
"""
it takes the name of a state as an arg
and list all the cities of that state
using the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cr = db.cursor()
    cr.execute("""SELECT
                    cities.name
                    FROM cities INNER JOIN states
                    ON cities.state_id=states.id
                    WHERE states.name=%s ORDER BY cities.id""", (statename,))

    rows = cr.fetchall()
    for row in rows:
        for col in row:
            print(col, end='')
        if rows.index(row) < len(rows) - 1:
            print(end=', ')

    print()
    cr.close()
    db.close()
