#!/usr/bin/python3
""" Fetch all modle """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    format_string = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(format_string.format(sys.argv[1],
                           sys.argv[2],
                           sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State, City).filter(
            State.id == City.state_id).order_by(
                    City.id.asc()).all()
    for (state, city) in result:
        print(f"{state.name}: ({city.id}) {city.name}")
