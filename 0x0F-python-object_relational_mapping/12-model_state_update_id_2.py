#!/usr/bin/python3
# coding = 'utf-8'
"""
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_state(_usr, _pass, _db):
    # Create the engine
    sql_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql_url.format(_usr, _pass, _db))

    # Configure the session & Create tables
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    res = session.query(State).filter(State.id == 2).first()
    res.name = 'New Mexico'
    session.commit()

    session.close()


if __name__ == "__main__":
    update_state(argv[1], argv[2], argv[3])
