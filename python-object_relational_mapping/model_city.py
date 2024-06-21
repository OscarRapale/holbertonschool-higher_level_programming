#!/usr/bin/python3
"""
Contains City class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                 nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
