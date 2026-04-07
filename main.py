from fastapi import FastAPI
from weather import get_zurich_weather
from database import SessionLocal, Note
from anthropic import Anthropic
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

app = FastAPI()

class SummarizeRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Hello from your first API"}

@app.get("/weather/live")
def live_weather():
    return get_zurich_weather()

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/notes")
def get_notes():
    db = SessionLocal()
    notes = db.query(Note).all()
    db.close()
    return notes

@app.post("/notes")
def create_note(title: str, content: str):
    db = SessionLocal()
    note = Note(title=title, content=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    db.close()
    return note



@app.post("/summarize")
def summarize(request: SummarizeRequest):
    try:
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": f"Summarize this concisely: {request.text}"}
            ]
        )
        return {"summary": message.content[0].text}
    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}