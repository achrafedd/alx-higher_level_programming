#!/usr/bin/python3
''' model state fetch all '''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).filter(
        State.name == argv[4]
        ).order_by(State.id).first()
    if state:
        print(state.id)
    else:
        print('Not found')
