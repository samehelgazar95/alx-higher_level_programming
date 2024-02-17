#!/usr/bin/python3
# coding = 'utf-8'
"""
Inserting new state & updating it's id
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def insert_state(_usr, _pass, _db):
    # Create the engine
    sql_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql_url.format(_usr, _pass, _db))

    # Configure the session & Create tables
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    new_state = State('Louisiana')
    session.add(new_state)
    session.commit()

    res = session.query(State).filter(State.name == 'Louisiana').first()
    print(res.id)

    session.close()


if __name__ == "__main__":
    insert_state(argv[1], argv[2], argv[3])
