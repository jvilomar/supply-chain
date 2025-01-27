import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar variables de entorno
load_dotenv()

# Configurar el cliente de Supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def insert_product(name: str, description: str, price: float, stock: int):
    """Inserta un producto en la base de datos."""
    data, error = supabase.table("products").insert({
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }).execute()
    
    if error:
        print(f"Error al insertar producto: {error}")
    else:
        print(f"Producto '{name}' insertado correctamente.")

def list_products():
    """Lista todos los productos en la base de datos."""
    response = supabase.table("products").select("*").execute()
    
    if response.data:
        print("\nLista de productos:")
        for product in response.data:
            print(f"ID: {product['id']}")
            print(f"Nombre: {product['name']}")
            print(f"Descripción: {product['description']}")
            print(f"Precio: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("-" * 30)
    else:
        print("No se encontraron productos.")

def main():
    # Insertar productos de prueba
    insert_product("Laptop", "Laptop de alta gama", 999.99, 50)
    insert_product("Smartphone", "Último modelo de smartphone", 699.99, 100)
    insert_product("Auriculares Bluetooth", "Auriculares inalámbricos de calidad", 129.99, 200)

    # Listar todos los productos
    list_products()

if __name__ == "__main__":
    main()