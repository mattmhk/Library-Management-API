from fastapi import APIRouter, HTTPException
from schemas import MemberCreate, MemberUpdate
from storage import members

router = APIRouter(
    prefix="/members",
    tags=["Members"]
)

@router.get("")
def get_members():
    return members

@router.post("")
def add_member(member: MemberCreate):
    new_member = {
        "id": len(members) + 1,
        "name": member.name,
        "email": member.email
    }
    members.append(new_member)
    return {"message": "Member added successfully", "member": new_member}

@router.get("/{member_id}")
def get_member(member_id: int):
    for member in members:
        if member["id"] == member_id:
            return member
    raise HTTPException(status_code=404, detail="Member Not Found")

@router.put("/{member_id}")
def update_member(member_id: int, member_update: MemberUpdate):
    for member in members:
        if member["id"] == member_id:
            member["email"] = member_update.email
            return {"message": "Member Updated Successfully", "member": member}
    raise HTTPException(status_code=404, detail="Member Not Found")

@router.delete("/{member_id}")
def delete_member(member_id: int):
    for member in members:
        if member["id"] == member_id:
            members.remove(member)
            return {"message": "Member Deleted Successfully", "member": member}
    raise HTTPException(status_code=404, detail="Member Not Found.")
