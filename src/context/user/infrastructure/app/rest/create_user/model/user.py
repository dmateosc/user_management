from datetime import datetime
from pydantic import BaseModel

class UserRequest(BaseModel):
  name: str
  last_name: str
  phone: int
  last_date: str
  active: bool
  
  
class UserResponse(BaseModel):
  name: str
  last_name: str
  phone: int
  last_date: str
  active: bool
   