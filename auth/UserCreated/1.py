from pydantic import BaseModel, Field


class UserV1(BaseModel):
    public_id: str
    role: str


class UserCreatedV1(BaseModel):
    event_name: str = Field("User.Created", const=True)
    data: UserV1
