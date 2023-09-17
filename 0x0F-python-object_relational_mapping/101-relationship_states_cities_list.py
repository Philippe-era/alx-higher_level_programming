#!/usr/bin/python3

""" all states will be listed  """
""" state introduced with relationship on th eline """
if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import Base, State

    input_check = sys.argv
    if len(input_check) < 4:
        exit(1)

    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()
    my_query_execute = session.query(State) \
                      .order_by(State.id) \
                      .all()
    for state in my_query_execute:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
