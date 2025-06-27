#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
import os
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_host = os.getenv('HBTN_MYSQL_HOST', 'localhost')
    db_user = sys.argv[1]
    db_pwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_pwd}@{db_host}:3306/{db_name}',
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).join(City).order_by(City.id)

    for state, city in query.all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
