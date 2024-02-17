#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://root:root@localhost:port/dbname')
Session = sessionmaker(bind=engine)
Base = declarative_base()

