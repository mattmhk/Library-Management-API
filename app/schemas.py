from pydantic import BaseModel, Field, EmailStr


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    quantity: int = Field(ge=0)


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    quantity: int

    class Config:
        from_attributes = True


class MemberCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr


class MemberUpdate(BaseModel):
    email: EmailStr


class MemberResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class BorrowCreate(BaseModel):
    book_id: int = Field(ge=1)
    member_id: int = Field(ge=1)


class BorrowResponse(BaseModel):
    id: int
    book_id: int
    member_id: int
    borrowed_at: str
    returned_at: str = None

    class Config:
        from_attributes = True


class BookQuantityUpdate(BaseModel):
    quantity: int = Field(ge=0)   