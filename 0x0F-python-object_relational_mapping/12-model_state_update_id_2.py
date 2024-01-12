#!/usr/bin/python3
"""
script to change the name of a state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]
                            ), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    ses = Session(eng)

    st = ses.query(State).filter(State.id == 2).first()
    st.name = "New Mexico"
    ses.commit()
    ses.close()
