#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
import os
from model_state import Base, State
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

    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
