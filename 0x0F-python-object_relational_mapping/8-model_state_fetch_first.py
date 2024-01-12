#!/usr/bin/python3
"""
it takes the firth object from
the database and prints it
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]
                            ), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    session = Session(eng)
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing')
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
