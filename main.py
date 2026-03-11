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

jugadores = [
    Jugador(id=1, name="Messi", dorsal=10, altura=1.70, posicion="DELANTERO", equipo="Inter Miami"),
    Jugador(id=2, name="Ronaldo", dorsal=7, altura=1.87, posicion="DELANTERO", equipo="Al Nassr"),
]

@app.get("/")
def home():
    return {"mensaje": "API de jugadores funcionando"}

@app.get("/players")
def get_players():
    return jugadores