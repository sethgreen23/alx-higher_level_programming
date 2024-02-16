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
    conn = MySQLdb.connect(host=HT,
                           port=PORT,
                           user=USER,
                           passwd=PASS,
                           db=DB, charset=CT)
    cur = conn.cursor()
    query_line = "SELECT cities.id, cities.name, states.name FROM \
            cities INNER JOIN states ON \
            cities.state_id = states.id ORDER BY cities.id ASC;"
    cur.execute(query_line)
    query_rows = cur.fetchall()
    for row in query_rows:
        (id, city, state) = row
        print((id, city, state))
    cur.close()
    conn.close()
