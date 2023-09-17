#!/usr/bin/python3
""" Will print the first State object from the db """
""" state fetch """
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
    object_create= session.query(State).first()
    if object_create is None:
        print("Nothing")
    else:
        print(object_create.id, object_create.name, sep=": ")
