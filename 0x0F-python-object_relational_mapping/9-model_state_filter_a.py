#!/usr/bin/python3
"""
this lists all State objects that begin with a
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
    ses = Session(eng)
    for state in ses.query(State).order_by(
                State.id).filter(State.name.contains('a')).all():
        print("{}: {}".format(state.id, state.name))
    ses.close()
