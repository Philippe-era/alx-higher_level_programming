""" Writing a script which list all State objects """
""" State fetch """

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    input_check = sys.argv
    if len(input_check) < 4:
        exit(1)
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    session_new = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session_new = Session()

    output_display = session_new.query(State).order_by(State.id).all()
    for state in output_display:
        print("{}: {}".format(state.id, state.name))

    session_new.close()
