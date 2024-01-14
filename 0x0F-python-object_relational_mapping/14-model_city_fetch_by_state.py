#!/usr/bin/python3
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    rows = session.query(City.id, City.name, State.name.label('state')).join(State, City.state_id == State.id).order_by(City.id).all()
    for city in rows:
        print(f"{city.state}: ({city.id}) {city.name}")
