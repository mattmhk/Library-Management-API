from fastapi import FastAPI

app = FastAPI()

books = []


@app.get("/")
def home():
    return {"message": "The Library API is running."}


@app.get("/books")
def getBooks():
    return books


@app.post("/books")
def addBook(title: str, author: str, quantity: int):
    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "quantity": quantity
    }

    books.append(book)
    return {"message": "Book has been added successfully.", "book": book}


@app.get("/books/{bookid}")
def getBook(bookid: int):
    for book in books:
        if book["id"] == bookid:
            return book

    return {"message": "Book not found."}


@app.put("/books/updatequantity/{bookid}")
def updateBookQuantity(bookid: int, quantity: int):
    for book in books:
        if book["id"] == bookid:
            book["quantity"] = quantity
            return {"message": "The quantity of the book has been successfully updated.", "book": book}

    return {"message": "Book not found."}


@app.delete("/books/delete/{bookid}")
def deleteBook(bookid: int):
    for book in books:
        if book["id"] == bookid:
            books.remove(book)
            return {"message": "The book has been successfully deleted."}

    return {"message": "Book not found."}