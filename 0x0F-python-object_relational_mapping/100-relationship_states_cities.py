#!/usr/bin/python3
"""adds city to the mix you see how it goes"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # SQL achemy will be developed with creditails on check
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # table created to work with the information at hand
    Base.metadata.create_all(engine)

    #session created 
    Session = sessionmaker(bind=engine)

    #session object
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco", state=state)

    # adds new city into the mix
    session.add(state)
    session.add(city)

    #changes in the information at hand
    session.commit()

