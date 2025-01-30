from pydantic import BaseModel
from typing import List

class BranchBase(BaseModel):
    id: int
    name: str

class BankBase(BaseModel):
    id: int
    name: str
    branches: List[BranchBase] = []
