#!/usr/bin/python3
""" model city """
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ class city """
    __tablename__ = "cities"
    id = Column(
        'id',
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False)
    name = Column('name',
                  String(128),
                  nullable=False)
    state_id = Column('state_id',
                      Integer,
                      ForeignKey('states.id'),
                      nullable=False)
