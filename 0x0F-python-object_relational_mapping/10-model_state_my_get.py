#!/usr/bin/python3
# coding = 'utf-8'
"""
Search for a specific state
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def search_for_states(_usr, _pass, _db, _state):
    # Create the engine
    sql_url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(sql_url.format(_usr, _pass, _db))

    # Configure the session & Ceate tables
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()
    result = session.query(State).filter(State.name == str(_state)).first()

    if result:
        print("{}".format(result.id))
    else:
        print('Not Found')


if __name__ == '__main__':
    search_for_states(argv[1], argv[2], argv[3], argv[4])
