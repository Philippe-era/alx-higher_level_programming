
#!/usr/bin/python3
"""the blueprint for the relationship input in check"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

# Create the base class for the declarative models
Base = declarative_base()

class State(Base):
    """The database created

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): The states identity been checked
        name (sqlalchemy.String): name of the state in check
        cities (sqlalchemy.orm.relationship): relationship status in check and inputted
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # relationship between the two 
    cities = relationship("City", backref="state", cascade="all, delete")


