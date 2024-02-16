#!/usr/bin/python3
"""List States Starting with 'N'"""
import MySQLdb
import sys


def list_state_n(user_name, password, db_name):
    qry = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         charset='utf8',
                         user=user_name,
                         password=password,
                         db=db_name)
    curs = db.cursor()
    curs.execute(qry)
    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()
    db.close()


if __name__ == "__main__":
    list_state_n(sys.argv[1], sys.argv[2], sys.argv[3])
