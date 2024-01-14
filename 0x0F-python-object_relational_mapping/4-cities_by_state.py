#!/usr/bin/python3
""" select all cities """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM cities AS c
                INNER JOIN states AS s
                WHERE c.state_id = s.id
                ORDER BY c.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
