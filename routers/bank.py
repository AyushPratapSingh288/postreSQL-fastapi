from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db_config.db import SessionLocal
from crud import create_bank, get_banks, get_bank_by_id, update_bank, delete_bank
from schema import BankBase

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_bank(bank: BankBase, db: Session = Depends(get_db)):
    return create_bank(db, bank)

@router.get("/")
def list_banks(db: Session = Depends(get_db)):
    return get_banks(db)

@router.get("/{bank_id}")
def get_bank(bank_id: int, db: Session = Depends(get_db)):
    bank = get_bank_by_id(db, bank_id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")
    return bank

@router.put("/{bank_id}")
def modify_bank(bank_id: int, name: str, db: Session = Depends(get_db)):
    updated_bank = update_bank(db, bank_id, name)
    if not updated_bank:
        raise HTTPException(status_code=404, detail="Bank not found")
    return updated_bank

@router.delete("/{bank_id}")
def remove_bank(bank_id: int, db: Session = Depends(get_db)):
    deleted_bank = delete_bank(db, bank_id)
    if not deleted_bank:
        raise HTTPException(status_code=404, detail="Bank not found")
    return {"message": "Bank deleted successfully"}
