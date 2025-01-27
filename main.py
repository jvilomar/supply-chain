from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
import os

# Configuración de Supabase
url = os.getenv("SUPABASE_URL")
key = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")
supabase: Client = create_client(url, key)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Modelo para crear productos
class Producto(BaseModel):
    nombre: str
    cantidad_disponible: int
    id_almacen: int

@app.post("/productos")
async def create_producto(producto: Producto):
    response = supabase.table("productos").insert(producto.model_dump()).execute()
    if response.error:
        raise HTTPException(status_code=400, detail="Error creando el producto.")
    return response.data

@app.get("/productos")
async def get_productos():
    response = supabase.table("productos").select("*").execute()
    return response.data

# Aquí puedes agregar más endpoints para manejar almacenes, pedidos, tracking, etc.