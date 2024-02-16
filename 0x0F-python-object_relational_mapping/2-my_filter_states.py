#!/usr/bin/python3
"""List States equals to argv[4]"""
import MySQLdb
import sys


def list_state_n(user_name, password, db_name, state_name):
    qry = "SELECT * FROM states \
           WHERE states.name = '{s_name}' \
           ORDER BY states.id ASC".format(s_name=state_name)
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
    args = sys.argv
    list_state_n(args[1], args[2], args[3], args[4])
