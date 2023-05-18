from pydantic import BaseModel, Field 


class UserRegistration(BaseModel):
    username: str
    password: str
    name: str

class ItemCreation(BaseModel):
    ... # TODO: Create schema for item creation
