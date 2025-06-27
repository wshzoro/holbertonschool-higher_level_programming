"""
Prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
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
    state_name_search = sys.argv[4]

    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_pwd}@{db_host}:3306/{db_name}',
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name_search).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
