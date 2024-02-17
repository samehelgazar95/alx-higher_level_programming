#!/usr/bin/python3
# coding = 'utf-8'
"""
Print the first state if found
or Nothing if not found
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


def first_state(myUser, myPass, myDb):

    # Create the engine
    sql_url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(sql_url.format(myUser, myPass, myDb))

    # Creating the tables
    Base.metadata.create_all(engine)

    # Configure the session
    Session = sessionmaker(bind=engine)

    # Start a session
    session = Session()
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print('Nothing')


if __name__ == "__main__":
    first_state(argv[1], argv[2], argv[3])
