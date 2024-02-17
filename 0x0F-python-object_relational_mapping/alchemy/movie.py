#!/usr/bin/python3
# coding = utf-8

from sqlalchemy import Column, String, Integer, Date
from base import Base


movies_actors_association = Table(
        'movies_actors', Base.metadata,
        Column('movie_id', ForeignKey('movies.id')),
        Column('actor_id', ForeignKey('actor.id'))
        )

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    # Constructor
    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date
