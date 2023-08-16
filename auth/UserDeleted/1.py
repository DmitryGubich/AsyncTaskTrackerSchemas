from pydantic import BaseModel, Field


class UserV1(BaseModel):
    public_id: str


class UserDeletedV1(BaseModel):
    event_name: str = Field("User.Deleted", const=True)
    data: UserV1
