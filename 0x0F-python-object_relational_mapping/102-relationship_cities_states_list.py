#!/usr/bin/python3
""" Fetch all modle that make get what you want from state and city """


if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    format_string = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(format_string.format(sys.argv[1],
                           sys.argv[2],
                           sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City).\
        outerjoin(State).\
        order_by(City.id).\
        all()
    for city in result:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
