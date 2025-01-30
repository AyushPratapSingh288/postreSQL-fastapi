from fastapi import FastAPI
from db_config.db import engine, Base
from routers import bank, branch
import uvicorn

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(bank.router, prefix="/banks", tags=["Banks"])
app.include_router(branch.router, prefix="/branches", tags=["Branches"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
