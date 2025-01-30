from sqlalchemy.orm import Session
from models.model import Bank, Branch
from schema import BankBase, BranchBase

def create_bank(db: Session, bank: BankBase):
    db_bank = Bank(name=bank.name)
    db.add(db_bank)
    db.commit()
    db.refresh(db_bank)
    return db_bank

def create_branch(db: Session, branch: BranchBase, bank_id: int):
    db_branch = Branch(name=branch.name, bank_id=bank_id)
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch

def get_banks(db: Session):
    return db.query(Bank).all()

def get_bank_by_id(db: Session, bank_id: int):
    return db.query(Bank).filter(Bank.id == bank_id).first()

def get_branches(db: Session):
    return db.query(Branch).all()

def get_branch_by_id(db: Session, branch_id: int):
    return db.query(Branch).filter(Branch.id == branch_id).first()

def update_bank(db: Session, bank_id: int, name: str):
    db_bank = db.query(Bank).filter(Bank.id == bank_id).first()
    if db_bank:
        db_bank.name = name
        db.commit()
        db.refresh(db_bank)
    return db_bank

def update_branch(db: Session, branch_id: int, name: str):
    db_branch = db.query(Branch).filter(Branch.id == branch_id).first()
    if db_branch:
        db_branch.name = name
        db.commit()
        db.refresh(db_branch)
    return db_branch

def delete_bank(db: Session, bank_id: int):
    db_bank = db.query(Bank).filter(Bank.id == bank_id).first()
    if db_bank:
        db.delete(db_bank)
        db.commit()
    return db_bank

def delete_branch(db: Session, branch_id: int):
    db_branch = db.query(Branch).filter(Branch.id == branch_id).first()
    if db_branch:
        db.delete(db_branch)
        db.commit()
    return db_branch
