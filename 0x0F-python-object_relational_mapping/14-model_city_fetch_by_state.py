#!/usr/bin/python3
""" THE CITY INFORMATION TO BE INCLUDED """
""" GET CITY INFORMATION FROM DATABASE """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance_create in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(instance_create[0] + ": (" + str(instance_create[1]) + ") " + instance_create[2])
