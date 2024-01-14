#!/usr/bin/python3

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2])

    cur = db.cursor()

    cur.execute('CREATE DATABASE IF NOT EXISTS {}'.format(argv[3]))

    cur.execute('USE {}'.format(argv[3]))

    cur.execute('''CREATE TABLE IF NOT EXISTS states (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
    )''')

    cur.execute('''INSERT INTO states (name)
        VALUES  ("California"),
                ("Arizona"),
                ("Texas"),
                ("New York"),
                ("Nevada")''')

    cur.execute('SELECT * from states ORDER BY id ASC')

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
