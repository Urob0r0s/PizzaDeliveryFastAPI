from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]
    
    
class Config:
    orm_mode = True
    schema_extra = {
        'example':{
            'username': 'alex',
            'email': 'alexlvov@mail.com',
            'password': 'password',
            'is_staf': False,
            'is_active': True
        }
    }