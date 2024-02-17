#!/usr/bin/python3
"""Create declarative_base Class & State Class (Table)"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer,
                autoincrement=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
