from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from model import get_db, Driver
from schemas import DriverSchema

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
def add_drivers(driver: DriverSchema,session: Session = Depends(get_db)):
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
