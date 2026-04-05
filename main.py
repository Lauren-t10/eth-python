from fastapi import FastAPI
from weather import *

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