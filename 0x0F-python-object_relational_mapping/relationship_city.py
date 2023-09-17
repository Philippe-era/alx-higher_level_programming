#!/usr/bin/python3
"""defines the blueprint going forward ."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for the declarative models
Base = declarative_base()

class City(Base):
    """City is finished created involved

    Attributes:
        id (sqlalchemy.Column): the identity for the city at hand
        name (sqlalchemy.Column): the name for the city database
        state_id (sqlalchemy.Column): the idea is created you know
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)


