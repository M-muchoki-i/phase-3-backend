from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Text,Date
from datetime import date

class Base(DeclarativeBase):
    pass

class Driver(Base):
    __tablename__="drivers"
    id=Column(Integer(),primary_key=True)
    name=Column(Text)
    email=Column(Text)
    gender=Column(Text)
    id_number=Column(Integer)
    vehicle_id=Column(Integer)
    created_at = Column(Date, default=date.today)

class Vehicle(Base):
    __tablename__="vehicles"
    id =Column(Integer(),primary_key=True)
    No_plate=Column(Text)
    driver_id =Column(Text)
    route_id=Column(Text)
    created_at = Column(Date, default=date.today)

class Route(Base):
    __tablename__="routes"
    id=Column(Integer,primary_key=True)
    vehicle_id =Column(Integer)
    created_at = Column(Date, default=date.today)
