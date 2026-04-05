from fastapi import FastAPI
from weather import *
from database import SessionLocal, Note

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from your first API"}

@app.get("/weather/live")
def weather():
    return get_zurich_weather()


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/post/notes")
def create_note(title:str, content:str):
    db = SessionLocal()
    note = Note(title = title, content = content)
    db.add(note)
    db.commit()
    db.refresh(note)
    db.close()
    return note

@app.get("/get/notes")
def get_notes():
    db = SessionLocal()
    notes = db.query(Note).all()
    db.close()
    return notes