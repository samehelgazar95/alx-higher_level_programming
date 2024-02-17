#!/usr/bin/python3
"""
Creating a class for cities table
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class City(Base):
    """
    City class that inherits from Base
    And represents cities Table

    Attributes:
        id: city_id
        name: city_name
        state_id: state_id
        state: state parent
    """
    __tablename__ = 'cities'

    id = Column(
            Integer,
            autoincrement=True,
            nullable=False,
            primary_key=True)
    name = Column(
            String(128),
            nullable=False)
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False)
