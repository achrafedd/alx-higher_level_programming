#!/usr/bin/python3
""" select all cities """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT c.name FROM cities AS c
                INNER JOIN states AS s
                WHERE c.state_id = s.id
                AND s.name = %s
                ORDER BY c.id""", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        if row == rows[-1]:
            print(row[0])
        else:
            print(row[0], end=', ')
    cur.close()
    db.close()
