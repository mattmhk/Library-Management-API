from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()

books = []
members = []
class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    quantity: int = Field(ge=0)
    
class MemberCreate(BaseModel):
    name:str = Field(min_length=1)
    email: str = Field(min_length=1)

@app.get("/")
def home():
    return {"message": "The Library API is running."}

@app.get("/books")
def getBooks():
    return books


@app.post("/books")
def addBook(book:BookCreate):
    new_book = {
        "id": len(books)+1,
        "title": book.title,
        "author": book.author,
        "quantity": book.quantity
    }
    
    books.append(new_book)
    return {"message": "Book has been added successfully.", "book": new_book}


@app.get("/books/{bookid}")
def getBook(bookid: int):
    for book in books:
        if book["id"] == bookid:
            return book

    raise HTTPException(status_code=404, detail="Book Not Found")


@app.put("/books/{bookid}")
def updateBookQuantity(bookid: int, quantity: int):
    for book in books:
        if book["id"] == bookid:
            book["quantity"] = quantity
            return {"message": "The quantity of the book has been successfully updated.", "book": book}

    raise HTTPException(status_code=404, detail="Book Not Found")

@app.delete("/books/{bookid}")
def deleteBook(bookid: int):
    for book in books:
        if book["id"] == bookid:
            books.remove(book)
            return {"message": "The book has been successfully deleted."}

    raise HTTPException(status_code=404, detail="Book Not Found")



@app.get("/members")
def getMembers():
    return members

@app.post("/members")
def addMember(member:MemberCreate):
    newMember={
        "id" : len(members)+1,
        "name" : member.name,
        "email" : member.email
    }
    members.append(newMember)
    return {"message":"Member added successfully","member":newMember}

@app.get("/members/{memberid}")
def getMember(memberid:int):
    for member in members:
        if member["id"]==memberid:
            return member
    raise HTTPException(status_code=404, detail="Member Not Found")

@app.put("/members/{memberid}")
def updateMember(memberid:int,email:str):
    for member in members:
        if member["id"]==memberid:
            member["email"]=email
            return {"message":"Member Updated Successfully","member":member}
    raise HTTPException(status_code=404, detail="Member Not Found")

@app.delete("/members/{memberid}")
def deleteMember(memberid:int):
    for member in members:
        if member["id"]==memberid:
            members.remove(member)
            return {"message":"Member Deleted Successfully","member":member}
    raise HTTPException(status_code=404,detail="Member Not Found")



    
            