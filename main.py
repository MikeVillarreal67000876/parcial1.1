from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class PosicionFutbol(str, Enum):
    PORTERO = "PORTERO"
    DEFENSA = "DEFENSA"
    MEDIOCAMPISTA = "MEDIOCAMPISTA"
    DELANTERO = "DELANTERO"
    EXTREMO = "EXTREMO"

class Jugador(BaseModel):
    id: int
    name: str
    dorsal: int
    altura: float
    posicion: PosicionFutbol
    equipo: str

@app.get("/")
def home():
    return {"mensaje": "API de jugadores funcionando"}