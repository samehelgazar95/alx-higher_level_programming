:#!/usr/bin/python3
# coding = utf-8

from base import Base
from actor import Actor
from contact_details import ContactDetails
from movie import Movie

session = Session()

movies = session.query(Movie).all()

for mov in movies:
    print(f'{mov.title} was released on {mov.release_date}')

movies2 = session.query(Movie).filter(Movie.release_date > date(2015, 1, 2)).all()

movies_dwayne = session.query(Movie).join(Actor, Movie.actors) \
        .filter(Actor.name == 'Dwayne Johnson').all()

glendale_stars = session.query(Actor).join(ContactDetails) \
        .filter(ContactDetails.address.ilike('%glendale%')).all()

# Get all data
actors_all = session.query(Actor)

# Get data in order
actors_ordered = session.query(Actor).order_by(Actor.name)

# Get data by filtering
actors_filtered = sesssion.query(Actor).filter(Actor.name=="Sameh").first()
actors_filter_or = session.query(Actor) \
        .filter(or_(Actor.name=="Sameh", Actor.name=="Gazar"))

# Count the number of results
actors_count = sesssion.query(Actor).filter(Actor.name=="Sameh").count()
actors_count_or = session.query(Actor) \
        .filter(or_(Actor.name=="Sameh", Actor.name=="Gazar")).count()

# Update data: Get > Update > Commit
actor_update = sesssion.query(Actor).filter(Actor.name=="Sameh").first()
actor_update.name = "ElGazar"
session.commit()

# Delete: Get > Delete > Commit
actor_delete = sesssion.query(Actor).filter(Actor.name=="Sameh").count()
session.delete(actor_delete)

