#!/usr/bin/python3
"""
this will hopefully list all the cities in
the data base
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cr = db.cursor()
    cr.execute("""SELECT cities.id,
                    cities.name, states.name
                    FROM cities INNER JOIN states
                    ON cities.state_id=states.id """)
    rows = cr.fetchall()
    for row in rows:
        print(row)

    cr.close()
    db.close()
