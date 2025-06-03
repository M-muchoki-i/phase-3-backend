from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from model import get_db, Driver, Vehicle,Passanger
from schemas import DriverSchema
from schemas import PassangerSchema
from schemas import VehicleSchema
from schemas import PassangerSchema

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/")
def index():
    return {"Message": "welcome to app"}


@app.get("/drivers")
def drivers(session: Session = Depends(get_db)):
    drivers = session.query(Driver).all()
    return drivers


@app.post("/drivers")
def add_drivers(driver: DriverSchema, session: Session = Depends(get_db)):
    # new_driver=Driver(name=driver.name,email=driver.email,gender=driver.gender,id_number=driver.id_number,vehicle_id=driver.vehicle_id)
    new_driver = Driver(**driver.model_dump())
    session.add(new_driver)
    session.commit()
    print(driver)

    return {"message": "driver added succesfully"}


@app.get("/drivers/{id}")
def get_drivers(id: int):
    print("Driver id", id)
    return {}


@app.patch("/drivers/{id}")
def update_drivers(id: int):
    print("driver_id", id)
    return {"message": "cretaed sucessfully"}


@app.get("/vehicles")
def vehicles(session: Session = Depends(get_db)):
    vehicles = session.query(Vehicle).all()
    return vehicles


@app.post("/vehicles")
def add_vehicles(vehicle: VehicleSchema, session: Session = Depends(get_db)):
    # new_driver=Driver(name=driver.name,email=driver.email,gender=driver.gender,id_number=driver.id_number,vehicle_id=driver.vehicle_id)
    new_vehicle = Vehicle(**vehicle.model_dump())
    session.add(new_vehicle)
    session.commit()
    print(vehicle)

    return {"message": "vehicle added succesfully"}


@app.get("/vehicles/{id}")
def get_vehicles(id: int):
    print("Vehicle id", id)
    return {}


@app.patch("/vehicles/{id}")
def update_vehicles(id: int):
    print("vehicle_id", id)
    return {"message": "cretaed sucessfully"}


@app.get("/passangers")
def passangers(session: Session = Depends(get_db)):
    passangers = session.query(Passanger).all()
    return passangers

@app.post("/passangers")
def add_passangers(passanger: PassangerSchema, session: Session = Depends(get_db)):
    # new_driver=Driver(name=driver.name,email=driver.email,gender=driver.gender,id_number=driver.id_number,vehicle_id=driver.vehicle_id)
    new_passanger = Passanger(**passanger.model_dump())
    session.add(new_passanger)
    session.commit()
    print(passanger)

    return {"message": "passanger added succesfully"}

@app.get("/passangers/{id}")
def get_passangers(id: int):
    print("Passanger id", id)
    return {}


@app.patch("/passangers/{id}")
def update_passangers(id: int):
    print("passanger_id", id)
    return {"message": "cretaed sucessfully"}