#!/use/bin/python3
# coding - utf-8

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import Base

class Stuntman(Base):
    __tablename__ = 'stuntman'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Boolean)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relaionship("Actor", backref=('stuntman', uselist=False))

    def __inti__(self, name, active, actor):
        self.name = name
        self.active = active
        self.actor = actor
