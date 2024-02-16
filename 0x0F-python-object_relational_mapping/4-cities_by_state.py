#!/usr/bin/python3
""" Printing Cities and States """
import MySQLdb
import sys


def print_cities(myUSER, myPASS, myDB):
    qry = """
        SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """

    with MySQLdb.connect(
                host='localhost', port=3306,
                charset='utf8', passwd=myPASS,
                user=myUSER, db=myDB
                ) as conn:
        with conn.cursor() as cur:
            cur.execute(qry)

            results = cur.fetchall()
            for record in results:
                print(record)


if __name__ == "__main__":
    args = sys.argv
    print_cities(args[1], args[2], args[3])
