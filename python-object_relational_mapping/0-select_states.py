#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # récupération des arguments passés en ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # création d'un curseur pour exécuter les requêtes
    cur = db.cursor()

    # exécution de la requête SQL
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # fermeture du curseur et de la connexion
    cur.close()
    db.close()
