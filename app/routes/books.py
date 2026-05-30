from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Book
from schemas import BookCreate, BookQuantityUpdate, BookResponse


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get("", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@router.post("", response_model=BookResponse)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(
        title=book.title,
        author=book.author,
        quantity=book.quantity
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book Not Found")
    return book


@router.put("/{book_id}", response_model=BookResponse)
def update_book_quantity(book_id: int, book_quantity_update: BookQuantityUpdate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book Not Found")
    
    book.quantity = book_quantity_update.quantity
    db.commit()
    db.refresh(book)
    return book


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book Not Found")
    
    db.delete(book)
    db.commit()
    return {"message": "The book has been successfully deleted."}
