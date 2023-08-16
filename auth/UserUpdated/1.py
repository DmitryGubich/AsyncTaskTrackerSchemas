from pydantic import BaseModel, Field


class UserV1(BaseModel):
    public_id: str
    role: str


class UserUpdatedV1(BaseModel):
    event_name: str = Field("User.Updated", const=True)
    data: UserV1
