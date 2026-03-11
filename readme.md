# Parcial API Jugadores

Proyecto desarrollado con FastAPI para gestionar jugadores de futbol.

## Tecnologias
- Python
- FastAPI
- Uvicorn

## Como ejecutar
1. Crear entorno virtual
2. Activar entorno virtual
3. Instalar dependencias con:
   pip install -r requirements.txt
4. Ejecutar:
   python -m uvicorn main:app --reload

## Endpoints
- GET /
- GET /players
- GET /players/{player_id}
- GET /compare/{id1}/{id2}
- GET /team/{player_id}
- GET /players/team/{team}