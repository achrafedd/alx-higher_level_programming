#!/usr/bin/python3
''' relationship states cities list '''
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State)
    for state in states:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")
