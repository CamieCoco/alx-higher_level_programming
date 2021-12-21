#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities as city \
                    INNER JOIN states as state \
                    ON city.state_id = state.id \
                    ORDER BY city.id")
    print(", ".join([cities[2]
                    for cities in cur.fetchall() if cities[4] == sys.argv[4]]))
    db.close()
