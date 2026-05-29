from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import date


app = FastAPI()

books = []
members = []
borrows = []


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
    
    
@app.get("/")
def home():
    return {"message": "The Library API is running."}


@app.get("/books")
def get_books():
    return books


@app.post("/books")
def add_book(book: BookCreate):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "quantity": book.quantity
    }

    books.append(new_book)
    return {"message": "Book has been added successfully.", "book": new_book}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book Not Found")


@app.put("/books/{book_id}")
def update_book_quantity(book_id: int, quantity: int):
    for book in books:
        if book["id"] == book_id:
            book["quantity"] = quantity
            return {"message": "The quantity of the book has been successfully updated.", "book": book}

    raise HTTPException(status_code=404, detail="Book Not Found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "The book has been successfully deleted."}

    raise HTTPException(status_code=404, detail="Book Not Found")


@app.get("/members")
def get_members():
    return members

@app.post("/members")
def add_member(member: MemberCreate):
    new_member = {
        "id": len(members) + 1,
        "name": member.name,
        "email": member.email
    }
    members.append(new_member)
    return {"message": "Member added successfully", "member": new_member}

@app.get("/members/{member_id}")
def get_member(member_id: int):
    for member in members:
        if member["id"] == member_id:
            return member
    raise HTTPException(status_code=404, detail="Member Not Found")

@app.put("/members/{member_id}")
def update_member(member_id: int, email: str):
    for member in members:
        if member["id"] == member_id:
            member["email"] = email
            return {"message": "Member Updated Successfully", "member": member}
    raise HTTPException(status_code=404, detail="Member Not Found")

@app.delete("/members/{member_id}")
def delete_member(member_id: int):
    for member in members:
        if member["id"] == member_id:
            members.remove(member)
            return {"message": "Member Deleted Successfully", "member": member}
    raise HTTPException(status_code=404, detail="Member Not Found.")


@app.post("/borrow")
def borrow_book(borrow: BorrowCreate):
    member_found = False

    for member in members:
        if member["id"] == borrow.member_id:
            member_found = True
            break

    if not member_found:
        raise HTTPException(status_code=404, detail="Member not found.")

    book_found = False
    for book in books:
        if book["id"] == borrow.book_id:
            book_found = True
            if book["quantity"] > 0:
                book["quantity"] -= 1

                new_borrow = {
                    "id": len(borrows) + 1,
                    "book_id": borrow.book_id,
                    "member_id": borrow.member_id,
                    "borrowed_at": date.today(),
                    "returned_at": None
                }

                borrows.append(new_borrow)

                return {
                    "message": "New borrow has been sucessfully added",
                    "borrow": new_borrow
                }
            else:
                raise HTTPException(status_code=400, detail="No books are left to loan.")

    if not book_found:
        raise HTTPException(status_code=404, detail="Book not found.")
        
@app.post("/return/{borrow_id}")
def return_book(borrow_id: int):
    for borrow in borrows:
        if borrow["id"] == borrow_id:
            if borrow["returned_at"] is None:
                for book in books:
                    if book["id"] == borrow["book_id"]:
                        book["quantity"] += 1
                        borrow["returned_at"] = date.today()

                        return {
                            "message": "Loan has been sucessfully returned",
                            "borrow": borrow
                        }
            else:
                raise HTTPException(status_code=400, detail="The book has been returned already.")

    raise HTTPException(status_code=404, detail="Borrow not found")
