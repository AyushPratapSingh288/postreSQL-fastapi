from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db_config.db import SessionLocal
from crud import create_branch, get_branches, get_branch_by_id, update_branch, delete_branch
from schema import BranchBase

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{bank_id}")
def add_branch(bank_id: int, branch: BranchBase, db: Session = Depends(get_db)):
    return create_branch(db, branch, bank_id)

@router.get("/")
def list_branches(db: Session = Depends(get_db)):
    return get_branches(db)

@router.get("/{branch_id}")
def get_branch(branch_id: int, db: Session = Depends(get_db)):
    branch = get_branch_by_id(db, branch_id)
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch

@router.put("/{branch_id}")
def modify_branch(branch_id: int, name: str, db: Session = Depends(get_db)):
    updated_branch = update_branch(db, branch_id, name)
    if not updated_branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return updated_branch

@router.delete("/{branch_id}")
def remove_branch(branch_id: int, db: Session = Depends(get_db)):
    deleted_branch = delete_branch(db, branch_id)
    if not deleted_branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return {"message": "Branch deleted successfully"}
