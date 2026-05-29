from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()

books = []

class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    quantity: int = Field(ge=0)

@app.get("/")
def home():
    return {"message": "The Library API is running."}

@app.get("/books")
def getBooks():
    return books


@app.post("/books")
def addBook(book:BookCreate):
    for existing_book in books:
        if existing_book["id"]==book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists.")
    
    new_book = {
        "id": len(books)+1,
        "title": book.title,
        "author": book.author,
        "quantity": book.quantity
    }
    
    books.append(new_book)
    return {"message": "Book has been added successfully.", "book": book}


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