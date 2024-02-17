from alchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    comment = relationship("Comment")

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey=('articles.id'))

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)

class Tire(Base):
    __tablename__ = 'tires'

    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship('Car')

class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    mobile_phone = relationship("MobilePhone", uselist=False, back_populates="mobile_phones")

class MobilePhone(Base):
    __tablename__ = 'mobile_phones'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'))
    persons = relationship("People", back_populates="people")
    



Base.metadata.create_all(engine)


