# backend/app/main.py

from fastapi import FastAPI
from .routes import coders, admins, users

app = FastAPI(title="MindCode API", version="0.1")

# add routes
app.include_router(coders.router)
app.include_router(admins.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "¡Hola Pk! FastAPI está corriendo correctamente."}
