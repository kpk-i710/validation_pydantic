from  pydantic import  BaseModel

data = {
    "email": "abs@email",
    'bio': None,
    "age": 12
}


class UserSchema(BaseModel):
    email:str
    bio:str
    age:str


def func(data_: dict):
    data_["age"] += 1