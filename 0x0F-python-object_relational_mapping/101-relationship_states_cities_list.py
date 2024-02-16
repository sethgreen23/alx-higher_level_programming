#!/usr/bin/python3
""" Fetch all modle """

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    format_string = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(format_string.format(sys.argv[1],
                           sys.argv[2],
                           sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).\
        join(State.cities).\
        order_by(State.id, City.id).all()
    for state in result:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
