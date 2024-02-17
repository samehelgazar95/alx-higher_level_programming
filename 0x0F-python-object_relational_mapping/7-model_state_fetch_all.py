#!/usr/bin/python3
# coding = 'utf-8'

"""
List data from states using SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


def list_state(myUser, myPass, myDb):
    # Create Engine
    sql_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql_url.format(myUser, myPass, myDb))

    # Configure the Session
    Session = sessionmaker(bind=engine)

    # Create a Session
    Base.metadata.create_all(engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    list_state(argv[1], argv[2], argv[3])
