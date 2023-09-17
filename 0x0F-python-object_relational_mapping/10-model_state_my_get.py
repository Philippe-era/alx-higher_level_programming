""" state my_get """

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    input_check = sys.argv
    if len(input_check) < 5 or ";" in input_check[4]:
        exit(1)

    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(input_check[1], input_check[2], input_check[3]))
    Session = sessionmaker(engine)

    Base.metadata.create_all(engine)

    session = Session()

    my_query_execute = session.query(State).filter(State.name.like(input_check[4])).all()

    if len(my_query_execute) == 0:
        print("Not found")
    else:
        print(my_query_execute[0].id)

    session.close()
