#!/usr/bin/python3
"""Print States"""
import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv[1:]
    qry = "SELECT * FROM states ORDER BY states.id ASC"

    db = MySQLdb.connect(
                        host='localhost',
                        port=3306,
                        user=args[0],
                        password=args[1],
                        db=args[2],
                        charset='utf8')
    cursor = db.cursor()
    cursor.execute(qry)

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
