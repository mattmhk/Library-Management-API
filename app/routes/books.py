from fastapi import APIRouter, HTTPException
from storage import books
from schemas import BookCreate, BookQuantityUpdate, MemberUpdate


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get("")
def get_books():
    return books


@router.post("")
def add_book(book: BookCreate):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "quantity": book.quantity
    }

    books.append(new_book)
    return {"message": "Book has been added successfully.", "book": new_book}


@router.get("/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book Not Found")


@router.put("/{book_id}")
def update_book_quantity(book_id: int, book_quantity_update: BookQuantityUpdate):
    for book in books:
        if book["id"] == book_id:
            book["quantity"] = book_quantity_update.quantity
            return {"message": "The quantity of the book has been successfully updated.", "book": book}

    raise HTTPException(status_code=404, detail="Book Not Found")


@router.delete("/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "The book has been successfully deleted."}

    raise HTTPException(status_code=404, detail="Book Not Found")
