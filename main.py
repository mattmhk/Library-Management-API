from fastapi import FastAPI


app=FastAPI();

books=[]

@app.get("/")
def home():
    return {"message":"The Library API is running."}

@app.get("/books")
def getBooks():
    return books


@app.get("/add")
def addBook(title:str,author:str,isbn:int,quantity:int):
    book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "quantity" : quantity
            }
    
    books.append(book)
    return "Book has been added successfully."

@app.get("/updatequantity")
def updateBookQuantity(title:str,quantity:int):
    for book in books:
        if book("title")==title:
            book("quantity"==quantity)
    return "The quantity of the book has been sucessfully updated."

@app.get("/delete")
def deleteBook(title:str):
    for book in books:
        if book("title")==title:
            books.remove(book)
    return "The book has been sucessfully deleted"

