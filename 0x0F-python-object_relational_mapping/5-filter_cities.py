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
    STATE = sys.argv[4]
    conn = MySQLdb.connect(host=HT,
                           port=PORT,
                           user=USER,
                           passwd=PASS,
                           db=DB, charset=CT)
    cur = conn.cursor()
    query_line = "SELECT cities.name FROM cities INNER JOIN states \
            ON cities.state_id = states.id AND \
            states.name=%s ORDER BY cities.id ASC;"
    cur.execute(query_line, (STATE,))
    query_rows = cur.fetchall()
    print(', '.join([city[0] for city in query_rows]))
    cur.close()
    conn.close()
