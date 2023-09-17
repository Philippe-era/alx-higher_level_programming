#!/usr/bin/python3

""" blueprint of the model class """

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata_check = MetaData()
Base = declarative_base(metadata=metadata_check)


class State(Base):

    """
    attributes class in check
    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
