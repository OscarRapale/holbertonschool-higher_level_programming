#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    query = argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (query, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
