#!/usr/bin/python3
# coding = utf-8

from sqlalchemy import Column, String, Integer, Date
from base import Base

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    # Constructor
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
