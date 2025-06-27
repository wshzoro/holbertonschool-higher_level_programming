#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

  
    db = MySQLdb.connect(
        host="db",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

   
    cur = db.cursor()

 
    cur.execute("SELECT * FROM states ORDER BY id ASC")

   
    for row in cur.fetchall():
        print(row)


    cur.close()
    db.close()
