#!/usr/bin/python3
"""
script should take 4 arguments: mysql username, mysql password, database
name and state name searched (safe from MySQL injection)
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT city.id, city.name, \
                    state.name FROM cities as \
                    city INNER JOIN states as state \
                    ON city.state_id = state.id \
                    ORDER BY city.id")
    for cities in cur.fetchall():
        print(cities)
    db.close()
