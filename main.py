from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API de jugadores funcionando"}
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class PosicionFutbol(str, Enum):
    PORTERO = "PORTERO"
    DEFENSA = "DEFENSA"
    MEDIOCAMPISTA = "MEDIOCAMPISTA"
    DELANTERO = "DELANTERO"
    EXTREMO = "EXTREMO"

@app.get("/")
def home():
    return {"mensaje": "API de jugadores funcionando"}