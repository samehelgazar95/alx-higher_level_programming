#!/usr/bin/python3
""" List all Cities in a specific state
    And handle the SQL Injenction
"""
import MySQLdb
import sys


def cities_of_state(myUser, myPass, myDb, state_name):
    qry = """
        SELECT name FROM cities
        WHERE state_id = (
            SELECT id FROM states
            WHERE name = %(state_name)s
        )
        ORDER BY cities.id ASC;
    """
    try:
        with MySQLdb.connect(
                host='localhost', port=3306,
                charset='utf8', user=myUser,
                passwd=myPass, db=myDb
                ) as conn:
            with conn.cursor() as cur:
                cur.execute(qry, {'state_name': state_name})
                results = ', '.join(city[0] for city in cur.fetchall())
                print(results)
    except MySQLdb.Error as e:
        print(f'MySQLdb Error: {e}')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    args = sys.argv
    cities_of_state(args[1], args[2], args[3], args[4])
