from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Base de datos en memoria (lista)
users_db = []

# Modelo de datos
class User(BaseModel):
    name: str
    age: int
    email: str

# Obtener todos los usuarios (GET)
@app.get("/users", response_model=List[User])
def get_users():
    return users_db

# Agregar un usuario (POST)
@app.post("/users")
def create_user(user: User):
    users_db.append(user)
    return {"message": "Usuario agregado correctamente", "user": user}
