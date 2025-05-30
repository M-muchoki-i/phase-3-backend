
from pydantic import BaseModel

class DriverSchema(BaseModel):
    name:str
    email:str
    gender:str
    id_number:int
    vehicle_id:int
   
