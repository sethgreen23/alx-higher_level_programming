#!/usr/bin/python3
""" Model state module """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ State class that describe the state schema"""

    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    name = Column(String(125), nullable=False)
