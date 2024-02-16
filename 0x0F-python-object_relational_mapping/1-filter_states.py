#!/usr/bin/python3
""" list all states from database hbtn_0e_0_usa"""


import sys
import MySQLdb


if __name__ == "__main__":
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]
    HT = "localhost"
    PORT = 3306
    CT = "utf8"
    conn = MySQLdb.connect(host=HT,
                           port=PORT,
                           user=USER,
                           passwd=PASS,
                           db=DB, charset=CT)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE \
            CAST(SUBSTR(states.name, 1, 1) AS BINARY) \
            REGEXP CAST('[N]' AS BINARY) \
            ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
