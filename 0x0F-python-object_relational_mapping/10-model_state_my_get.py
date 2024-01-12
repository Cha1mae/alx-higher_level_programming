#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    connection_string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database
    )
    eng = create_engine(
        connection_string,
        pool_pre_ping=True
    )
    Base.metadata.create_all(eng)

    ses = Session(eng)
    st = ses.query(State).filter(State.name == state_name).first()

    if st is None:
        print('Not found')
    else:
        print("{}".format(st.id))

    ses.close()


if __name__ == "__main__":
    main()
