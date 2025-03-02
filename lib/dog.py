from models import Dog, Base
from sqlalchemy import create_engine

# Define the database engine globally
engine = create_engine("sqlite:///dogs.db")

def create_table(base, engine):  # Accepts Base as a parameter
    base.metadata.create_all(engine)  # Uses the passed Base to create tables

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.get(Dog, id)  # Correct way to fetch by ID

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
