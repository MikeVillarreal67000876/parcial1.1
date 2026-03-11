from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API de jugadores funcionando"}

from enum import Enum

class PosicionFutbol(str, Enum):
    PORTERO = "PORTERO"
    DEFENSA = "DEFENSA"
    MEDIOCAMPISTA = "MEDIOCAMPISTA"
    DELANTERO = "DELANTERO"
    EXTREMO = "EXTREMO"