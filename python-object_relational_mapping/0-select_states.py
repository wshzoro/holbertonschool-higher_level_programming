#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base MySQL
    db = MySQLdb.connect(
        host="host.docker.internal",  # Important sur Mac avec Docker
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Préparer un curseur
    cursor = db.cursor()

    # Exécuter la requête SQL pour afficher tous les états triés par id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Afficher les résultats
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermer la connexion
    cursor.close()
    db.close()
