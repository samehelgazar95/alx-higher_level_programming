#!/usr/bin/python3
# coding = 'utf-8'
"""
Print all cities in the table
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def print_cities(myUser, myPass, myDb):
    # Create the engine
    sql_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    full_url = sql_url.format(myUser, myPass, myDb)
    engine = create_engine(full_url, pool_pre_ping=True)

    # Configure the Session & Create the tables
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    results = session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id)

    for res in results:
        print("{}: ({} {}".format(
            res.State.name,
            res.City.id,
            res.City.name
            ))

    session.close()


if __name__ == "__main__":
    print_cities(argv[1], argv[2], argv[3])
