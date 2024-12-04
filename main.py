from  pydantic import  BaseModel, Field, EmailStr

data = {
    "email": "abs@email.ru",
    'bio': None,
    "age": 12
}


class UserSchema(BaseModel):
    email:EmailStr
    bio:str | None = Field(max_length=1000)
    age: int = Field(ge=0,le=130)


def func(data_: dict):
    data_["age"] += 1

user = UserSchema(**data)
print(user.age)