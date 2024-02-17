#!/usr/bin/python3
"""
Printing data from states table
"""
import MySQLdb
import sys
from model_state import Base, State


def list_state(myUser, myPass, myDb):
    qry = """
        SELECT * FROM states
        ORDER BY id ASC
        """

    with MySQLdb.connect(
                        user=myUser,
                        passwd=myPass,
                        db=myDb,
                        host='localhost',
                        port=3306,
                        charset='utf8') as conn:
        with conn.cursor() as cur:
            cur.execute(qry)
            results = cur.fetchall()

            for res in results:
                print("{}: {}".format(res[0], res[1]))


if __name__ == "__main__":
    args = sys.argv
    list_state(args[1], args[2], args[3])
