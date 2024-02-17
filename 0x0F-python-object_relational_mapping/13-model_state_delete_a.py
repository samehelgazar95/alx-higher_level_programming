#!/usr/bin/python3
# coding = 'utf-8'
"""
Delete record and update the table
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_state(_usr, _pass, _db):
    # Create the engine
    sql_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql_url.format(_usr, _pass, _db))

    # Configure the Session & Create tables
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    results = session.query(State).filter(State.name.like('%a%')).all()

    for res in results:
        session.delete(res)
        session.commit()
    session.close()


if __name__ == "__main__":
    delete_state(argv[1], argv[2], argv[3])
