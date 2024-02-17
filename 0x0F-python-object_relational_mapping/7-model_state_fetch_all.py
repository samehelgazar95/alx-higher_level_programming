#!/usr/bin/python3
# coding = 'utf-8'

"""
List data from states using SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


def list_state(myUser, myPass, myDb):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}' \
            .format(myUser, myPass, myDb), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    args = sys.argv
    list_state(args[1], args[2], args[3])
