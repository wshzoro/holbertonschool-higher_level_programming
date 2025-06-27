#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Création d’un curseur
    cur = db.cursor()
    
    # Exécution de la requête
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Récupération et affichage des résultats
    for row in cur.fetchall():
        print(row)
    
    # Fermeture des connexions
    cur.close()
    db.close()
