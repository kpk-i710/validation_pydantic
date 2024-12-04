from  pydantic import  BaseModel, Field

data = {
    "email": "abs@email",
    'bio': None,
    "age": 12
}


class UserSchema(BaseModel):
    email:str
    bio:str | None
    age: int = Field(ge=0,le=130)


def func(data_: dict):
    data_["age"] += 1

print(UserSchema(**data))