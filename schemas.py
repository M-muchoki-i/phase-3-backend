
from pydantic import BaseModel

class DriverSchema(BaseModel):
    name:str
    email:str
    gender:str
    
    vehicle_type:str
   
