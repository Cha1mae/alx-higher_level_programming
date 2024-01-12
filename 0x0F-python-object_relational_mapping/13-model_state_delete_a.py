#!/usr/bin/python3
"""
all states with a in the names are deleted
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

    states_with_a = ses.query(State).filter(State.name.contains('a')).all()

    for st in states_with_a:
        ses.delete(st)

    ses.commit()
    ses.close()
