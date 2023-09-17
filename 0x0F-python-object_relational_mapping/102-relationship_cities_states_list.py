
#!/usr/bin/python3
"""retrieve information from the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":

    # command line information
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # connection to the database at hand created 
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # tables will be created before everything else
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    # creates session 
    session = Session()

    cities = session.query(City).join(State).order_by(City.id)

    # prints the information from the database
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # session close
    session.close()

