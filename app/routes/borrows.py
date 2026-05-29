from fastapi import APIRouter, HTTPException
from datetime import date
from storage import members,borrows,books
from schemas import BorrowCreate

router = APIRouter(
    prefix="/borrow",
    tags=["Borrows"]
)

@router.post("")
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
                    "message": "New borrow has been successfully added",
                    "borrow": new_borrow
                }
            else:
                raise HTTPException(status_code=400, detail="No books are left to loan.")

    if not book_found:
        raise HTTPException(status_code=404, detail="Book not found.")
        
@router.put("/return/{borrow_id}")
def return_book(borrow_id: int):
    for borrow in borrows:
        if borrow["id"] == borrow_id:
            if borrow["returned_at"] is None:
                for book in books:
                    if book["id"] == borrow["book_id"]:
                        book["quantity"] += 1
                        borrow["returned_at"] = date.today()

                        return {
                            "message": "Loan has been successfully returned",
                            "borrow": borrow
                        }
            else:
                raise HTTPException(status_code=400, detail="The book has been returned already.")

    raise HTTPException(status_code=404, detail="Borrow not found")
