#!/usr/bin/python3
''' model state fetch all '''
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = State(name='California')
    session.add(state)
    session.commit()
    city = City(name='San Francisco', state_id=state.id)
    session.add(city)
    session.commit()
    session.close()
