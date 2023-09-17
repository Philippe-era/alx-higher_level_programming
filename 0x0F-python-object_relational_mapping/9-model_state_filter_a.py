#!/usr/bin/python3

""" script which lists all State objects which contain a letter_A """
""" STATE IS BEING REPLICATED"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance_created in session.query(State).filter(State.name.like('%a%')):
        print(instance_created.id, instance_created.name, sep=": ")
