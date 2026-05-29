from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    quantity: int = Field(ge=0)


class MemberCreate(BaseModel):
    name: str = Field(min_length=1)
    email: str = Field(min_length=1)


class BorrowCreate(BaseModel):
    book_id: int = Field(ge=1)
    member_id: int = Field(ge=1)

class BookQuantityUpdate(BaseModel):
    quantity: int = Field(ge=0)
    

class MemberUpdate(BaseModel):
    email: str = Field(min_length=1)   