
from pydantic import BaseModel

class DriverSchema(BaseModel):
    name:str
    email:str
    gender:str
    vehicle_type:str
    
    vehicle_type:str
   
class VehicleSchema(BaseModel):
    No_plate:str
    vehicle_type:str
    driver_id:str
    vehicle_image:str

class PassangerSchema(BaseModel):
    name:str
    email:str
    No_plate:str
    vehicle_type:str
   
    
    
   