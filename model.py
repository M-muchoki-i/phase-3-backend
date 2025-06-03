from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, Text, Date, create_engine
from datetime import date
from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

engine = create_engine("sqlite:///Tracker.db", echo=True)
Session = sessionmaker(bind=engine)


def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()


class Base(DeclarativeBase):
    pass


class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer(), primary_key=True)
    name = Column(Text)
    email = Column(Text)

    vehicle_type = Column(Text)
    created_at = Column(Date, default=date.today)


class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer(), primary_key=True)
    No_plate = Column(Text)
    driver_id = Column(Text)
    vehicle_type = Column(Text)
    vehicle_image = Column(Text)

    created_at = Column(Date, default=date.today)

class Passanger(Base):
      __tablename__ = "passangers"
      id =Column(Integer(), primary_key=True)
      name=Column(Text)
      email=Column(Text)
      No_plate = Column(Text)
      Vehicle_type=Column(Text)
      
    
      