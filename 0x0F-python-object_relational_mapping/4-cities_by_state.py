#!/usr/bin/python3
""" Printing Cities and States """
import MySQLdb
import sys


def print_cities(myUSER, myPASS, myDB):
    conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                charset='utf8',
                passwd=myPASS,
                user=myUSER,
                db=myDB
            )

    cur = conn.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """)

    results = cur.fetchall()
    for record in results:
        print(record)

    cur.close()
    conn.close()


if __name__ == "__main__":
    args = sys.argv
    print_cities(args[1], args[2], args[3])
