from fastapi import APIRouter, Depends, HTTPException
from datetime import date
from sqlalchemy.orm import Session
from database import get_db
from models import Borrow, Book, Member
from schemas import BorrowCreate, BorrowResponse

router = APIRouter(
    prefix="/borrow",
    tags=["Borrows"]
)

@router.post("", response_model=BorrowResponse)
def borrow_book(borrow: BorrowCreate, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == borrow.member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found.")

    book = db.query(Book).filter(Book.id == borrow.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    
    if book.quantity <= 0:
        raise HTTPException(status_code=400, detail="No books are left to loan.")
    
    book.quantity -= 1
    
    new_borrow = Borrow(
        book_id=borrow.book_id,
        member_id=borrow.member_id,
        borrowed_at=date.today(),
        returned_at=None
    )
    
    db.add(new_borrow)
    db.commit()
    db.refresh(new_borrow)
    return new_borrow

        
@router.put("/return/{borrow_id}", response_model=BorrowResponse)
def return_book(borrow_id: int, db: Session = Depends(get_db)):
    borrow = db.query(Borrow).filter(Borrow.id == borrow_id).first()
    if not borrow:
        raise HTTPException(status_code=404, detail="Borrow not found")
    
    if borrow.returned_at is not None:
        raise HTTPException(status_code=400, detail="The book has been returned already.")
    
    book = db.query(Book).filter(Book.id == borrow.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    
    book.quantity += 1
    borrow.returned_at = date.today()
    
    db.commit()
    db.refresh(borrow)
    return borrow

@router.get("", response_model=list[BorrowResponse])
def get_borrows(db: Session = Depends(get_db)):
    return db.query(Borrow).all()

@router.get("/{borrow_id}", response_model=BorrowResponse)
def get_borrow(borrow_id: int, db: Session = Depends(get_db)):
    borrow = db.query(Borrow).filter(Borrow.id == borrow_id).first()
    if not borrow:
        raise HTTPException(status_code=404, detail="Borrow not found")
    return borrow

@router.get("/member/{member_id}", response_model=list[BorrowResponse])
def get_member_borrows(member_id: int, db: Session = Depends(get_db)):
    member_borrows = db.query(Borrow).filter(Borrow.member_id == member_id).all()
    if not member_borrows:
        raise HTTPException(status_code=404, detail="No borrows found for this member")
    return member_borrows

@router.get("/book/{book_id}", response_model=list[BorrowResponse])
def get_book_borrows(book_id: int, db: Session = Depends(get_db)):
    book_borrows = db.query(Borrow).filter(Borrow.book_id == book_id).all()
    if not book_borrows:
        raise HTTPException(status_code=404, detail="No borrows found for this book")
    return book_borrows
