#!/usr/bin/python3
# coding = 'utf-8'
"""
List all states that contain letter 'a'
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(myUser, myPass, myDb):
    # Create the engine
    sql_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql_url.format(myUser, myPass, myDb))

    # Creating tables & Configure Session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Create a session & query
    session = Session()
    result = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id)

    for res in result:
        print('{}: {}'.format(res.id, res.name))

    session.close()


if __name__ == "__main__":
    list_states(argv[1], argv[2], argv[3])
