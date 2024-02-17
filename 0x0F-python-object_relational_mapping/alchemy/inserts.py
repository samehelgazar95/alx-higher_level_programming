#!/usr/bin/python3
# coding = utf-8

from datetime import date
from base import engine, Session, Base
from actor import Actor
from movie import Movie
from contacts_details import ContactDetails
from stuntman import Stuntman

# Generate DataBase Schema
Base.metadata.createall()

# Create new session
session = Session()

# Create movies
bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
furious_7 = Movie("Furious 7", date(2015, 4, 2)) 
pain_and_gain = Movie("Pain & Gain", date(2013, 8, 23))

# Create actors
matt_damon = Actor("Matt Damon", date(1970, 10, 8))
dwayne_johnson = Actor("Dwayne_Johnson", date(1972, 5, 2))
mark_wahlberg = Actor("Mark Wahlberg", date(1971, 6, 5))

# Add actors to movies
bourne_identity.actors = [matt_damon]
furious_7 = [dwayne_johnson]
pain_and_gain = [dwayne_johnson, mark_wahlberg]

# Add contact details to actors
matt_contact = contactDetails("123 456 7890", "Cairo Egypt", matt_damon)
dwayne_contact = contatDetails("123 456 7890", "Cairo Egypt", dwayne_johnson)
dwayne_contact2 = contactDetails("123 456 7890", "Cairo Egypt", dwayne_johnson)
mark_contact = contactDetails("123 456 7890", "Cairo Egypt", mark_wahlberg)

# Create stuntman
matt_stuntman = Stuntman("John Doe", True, matt_damon)
dwayne_stuntman = Stuntman("John Doe", True, dwayne_johnson)
mark_stuntman = Stuntman("Richard Roe", True, mark_wahlberg)

# Persist data
session.add(bourne_identity)
session.add(furious_7)
session.add(pain_and_gain)

session.addall([matt_contact, dwayne_contact, dwayne_contact2, mark_contact])
session.addall([matt_stuntman, dwayne_stuntman, dwayne_stuntman2, mark_stuntman])

session.commit()
sessionc.close()
