#!/usr/bin/python3
"""
adds Louisiana to the data base
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

    nstate = State(name='Louisiana')

    ses.add(nstate)
    ses.commit()
    print("{}".format(nstate.id))
    ses.close()
