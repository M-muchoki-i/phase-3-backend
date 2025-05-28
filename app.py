
from fastapi import FastAPI,Depends
from model import get_db,Driver

app = FastAPI()


@app.get("/") 
def index():
    return{"Message":"welcome to app"}
@app.get('/drivers')
def drivers(session= Depends(get_db)):
    drivers = session.query(Driver).all()
    return drivers
@app.post('/drivers')
def add_drivers():
    return{"message":"driver added succesfully"}
@app.get('/drivers{id}')
def get_drivers(id:int):
    print("driver_id" ,id)
    return {}