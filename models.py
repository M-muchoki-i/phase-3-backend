from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Text

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