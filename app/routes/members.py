from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Member
from schemas import MemberCreate, MemberUpdate, MemberResponse


router = APIRouter(
    prefix="/members",
    tags=["Members"]
)

@router.get("", response_model=list[MemberResponse])
def get_members(db: Session = Depends(get_db)):
    return db.query(Member).all()

@router.post("", response_model=MemberResponse)
def add_member(member: MemberCreate, db: Session = Depends(get_db)):
    new_member = Member(
        name=member.name,
        email=member.email
    )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

@router.get("/{member_id}", response_model=MemberResponse)
def get_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member Not Found")
    return member

@router.put("/{member_id}", response_model=MemberResponse)
def update_member(member_id: int, member_update: MemberUpdate, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member Not Found")
    
    member.email = member_update.email
    db.commit()
    db.refresh(member)
    return member

@router.delete("/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member Not Found")
    
    db.delete(member)
    db.commit()
    return {"message": "Member Deleted Successfully"}
