from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

# Crear la aplicación FastAPI
app = FastAPI(title="API Jugadores Futbol")

# Enum con las posiciones de futbol
class PosicionFutbol(str, Enum):
    PORTERO = "PORTERO"
    DEFENSA = "DEFENSA"
    MEDIOCAMPISTA = "MEDIOCAMPISTA"
    DELANTERO = "DELANTERO"
    EXTREMO = "EXTREMO"

# Modelo Jugador
class Jugador(BaseModel):
    id: int
    name: str
    dorsal: int
    altura: float
    posicion: PosicionFutbol
    equipo: str

# Lista de jugadores de ejemplo
jugadores = [
    Jugador(id=1, name="Messi", dorsal=10, altura=1.70, posicion="DELANTERO", equipo="Inter Miami"),
    Jugador(id=2, name="Ronaldo", dorsal=7, altura=1.87, posicion="DELANTERO", equipo="Al Nassr"),
    Jugador(id=3, name="Sergio Ramos", dorsal=4, altura=1.84, posicion="DEFENSA", equipo="Sevilla"),
    Jugador(id=4, name="Courtois", dorsal=1, altura=2.00, posicion="PORTERO", equipo="Real Madrid"),
]

# Endpoint principal
@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de jugadores de futbol"}

# Mostrar todos los jugadores
@app.get("/players")
def get_players():
    return jugadores

# Mostrar un jugador por id
@app.get("/players/{player_id}")
def show_one_player(player_id: int):

    for jugador in jugadores:
        if jugador.id == player_id:
            return jugador

    return {"mensaje": "No se encontro el jugador"}

# Comparar dos jugadores por altura
@app.get("/compare/{id1}/{id2}")
def compare_two_players(id1: int, id2: int):

    j1 = next((j for j in jugadores if j.id == id1), None)
    j2 = next((j for j in jugadores if j.id == id2), None)

    if not j1 or not j2:
        return {"mensaje": "Jugador no encontrado"}

    if j1.altura > j2.altura:
        return {
            "mas_alto": j1,
            "mensaje": f"{j1.name} es mas alto que {j2.name}"
        }
    elif j2.altura > j1.altura:
        return {
            "mas_alto": j2,
            "mensaje": f"{j2.name} es mas alto que {j1.name}"
        }
    else:
        return {"mensaje": "Los dos jugadores tienen la misma altura"}

# Mostrar el equipo de un jugador
@app.get("/team/{player_id}")
def show_equipo(player_id: int):

    for jugador in jugadores:
        if jugador.id == player_id:
            return {"equipo": jugador.equipo}

    return {"mensaje": "Jugador no encontrado"}

# Mostrar jugadores por equipo
@app.get("/players/team/{team}")
def players_by_team(team: str):

    resultado = [j for j in jugadores if j.equipo.lower() == team.lower()]

    if not resultado:
        return {"mensaje": "No hay jugadores en ese equipo"}

    return resultado