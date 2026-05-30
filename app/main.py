from fastapi import FastAPI
from routes import books, members, borrows
from models import Base
from database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router)
app.include_router(members.router)
app.include_router(borrows.router)

@app.get("/")
def home():
    return {"message": "The Library API is running."}

