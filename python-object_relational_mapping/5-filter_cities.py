#!/usr/bin/python3
"""  lists all cities in state from the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
               JOIN states ON states.id=cities.state_id
               WHERE states.name=%s""", (argv[4],))

    rows = cur.fetchall()
    cities = list(row[0] for row in rows)
    print(*cities, sep=", ")
    cur.close()
    db.close()
