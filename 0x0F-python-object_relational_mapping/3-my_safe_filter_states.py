#!/usr/bin/python3
""" list all states from database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]
    HT = "localhost"
    PORT = 3306
    CT = "utf8"
    NAME = sys.argv[4]
    conn = MySQLdb.connect(host=HT,
                           port=PORT,
                           user=USER,
                           passwd=PASS,
                           db=DB, charset=CT)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE states.name=%s ORDER BY id ASC",
                (NAME,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
