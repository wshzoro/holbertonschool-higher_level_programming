#!/usr/bin/python3
import pymysql
MySQLdb = pymysql

import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="127.0.0.1",  # Le container MySQL expose ce port en local
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
