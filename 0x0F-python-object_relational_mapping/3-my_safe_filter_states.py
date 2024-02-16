#!/usr/bin/python3
"""List States equals to argv[4]
    But it is safe from MySQL injections!"""
import MySQLdb
import sys


def list_state_n(user_name, password, db_name, state_name):
    qry = """
                SELECT * FROM states
                WHERE name = %(state_name)s
                ORDER BY states.id ASC
            """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         charset='utf8',
                         user=user_name,
                         passwd=password,
                         db=db_name)
    curs = db.cursor()
    curs.execute(qry, {'state_name': state_name})
    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()
    db.close()


if __name__ == "__main__":
    list_state_n(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
