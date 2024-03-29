#!/usr/bin/python3
""" display information from the database """
""" insert into state """
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
    state_include = State(name='Louisiana')
    session.add(state_include)
    create_instance = session.query(State).filter_by(name='Louisiana').first()
    print(create_instance.id)
    session.commit()
