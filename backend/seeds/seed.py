import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models import db

categories_data = [
    {"name": "Electronica"},
    {"name": "Ropa"},
    {"name": "Hogar"},
    {"name": "Deportes"},
    {"name": "Alimentacion"},
]

# Las imagenes se manejan desde el frontend con un placeholder por defecto
# cuando imageUrl esta vacio
products_data = [
    {
        "name": "Audifonos Bluetooth",
        "description": "Audifonos inalambricos con cancelacion de ruido y bateria de 30 horas",
        "price": 49.99,
        "imageUrl": "",
        "stock": 25,
        "category": "Electronica",
    },
    {
        "name": "Teclado Mecanico RGB",
        "description": "Teclado mecanico con switches azules y retroiluminacion RGB personalizable",
        "price": 79.99,
        "imageUrl": "",
        "stock": 15,
        "category": "Electronica",
    },
    {
        "name": "Camiseta Deportiva",
        "description": "Camiseta de poliester transpirable para entrenamiento de alto rendimiento",
        "price": 24.50,
        "imageUrl": "",
        "stock": 40,
        "category": "Ropa",
    },
    {
        "name": "Chaqueta Impermeable",
        "description": "Chaqueta ligera resistente al agua con capucha ajustable y bolsillos",
        "price": 65.00,
        "imageUrl": "",
        "stock": 10,
        "category": "Ropa",
    },
    {
        "name": "Lampara LED Escritorio",
        "description": "Lampara de escritorio con tres niveles de brillo y puerto USB integrado",
        "price": 32.00,
        "imageUrl": "",
        "stock": 20,
        "category": "Hogar",
    },
    {
        "name": "Organizador de Cocina",
        "description": "Set de organizadores apilables para especias y utensilios de cocina",
        "price": 18.75,
        "imageUrl": "",
        "stock": 35,
        "category": "Hogar",
    },
    {
        "name": "Balon de Futbol Pro",
        "description": "Balon de futbol tamano 5 con costura termica y diseno profesional",
        "price": 35.00,
        "imageUrl": "",
        "stock": 30,
        "category": "Deportes",
    },
    {
        "name": "Banda de Resistencia Set",
        "description": "Set de 5 bandas elasticas con diferentes niveles de resistencia para ejercicio",
        "price": 15.99,
        "imageUrl": "",
        "stock": 50,
        "category": "Deportes",
    },
    {
        "name": "Cafe Molido Premium",
        "description": "Cafe de origen colombiano tostado medio con notas de chocolate y caramelo",
        "price": 12.50,
        "imageUrl": "",
        "stock": 60,
        "category": "Alimentacion",
    },
    {
        "name": "Mix de Frutos Secos",
        "description": "Mezcla de almendras, nueces, pistachos y arandanos deshidratados 500g",
        "price": 9.99,
        "imageUrl": "",
        "stock": 45,
        "category": "Alimentacion",
    },
]


def run_seed():
    print("Limpiando colecciones...")
    db["categories"].delete_many({})
    db["products"].delete_many({})

    print("Insertando categorias...")
    cat_result = db["categories"].insert_many(categories_data)

    cat_map = {}
    for i, cat in enumerate(categories_data):
        cat_map[cat["name"]] = cat_result.inserted_ids[i]

    print("Insertando productos...")
    for p in products_data:
        doc = {
            "name": p["name"],
            "description": p["description"],
            "price": p["price"],
            "imageUrl": p["imageUrl"],
            "stock": p["stock"],
            "categoryId": cat_map[p["category"]],
        }
        db["products"].insert_one(doc)

    print(f"Seed completado: {len(categories_data)} categorias, {len(products_data)} productos")


if __name__ == "__main__":
    run_seed()
