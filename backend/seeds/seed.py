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
        "imageUrl": "https://www.idcmayoristas.com/wp-content/uploads/2025/08/audifono-inalambrico-infinytek-zion-bt-5-4-ab5636-tg12b-17-010738-2.png",
        "stock": 25,
        "category": "Electronica",
    },
    {
        "name": "Teclado Mecanico RGB",
        "description": "Teclado mecanico con switches azules y retroiluminacion RGB personalizable",
        "price": 79.99,
        "imageUrl": "https://tecnomall.ec/wp-content/uploads/2023/06/Teclado-Bluetooth-Gamer-Redragon-Mecanico-Fizz-Pro-Preto-RGB-K616rGB_1677171494_gg-jpg.webp",
        "stock": 15,
        "category": "Electronica",
    },
    {
        "name": "Camiseta Deportiva",
        "description": "Camiseta de poliester transpirable para entrenamiento de alto rendimiento",
        "price": 24.50,
        "imageUrl": "https://proimago.com.ec/wp-content/uploads/2024/03/camiseta-deportiva-3.jpg",
        "stock": 40,
        "category": "Ropa",
    },
    {
        "name": "Chaqueta Impermeable",
        "description": "Chaqueta ligera resistente al agua con capucha ajustable y bolsillos",
        "price": 65.00,
        "imageUrl": "https://looop.rocks/wp-content/uploads/2025/05/Chaqueta-Impermeable-100-CICLON-Unisex-NEGRO.jpg.webp",
        "stock": 10,
        "category": "Ropa",
    },
    {
        "name": "Lampara LED Escritorio",
        "description": "Lampara de escritorio con tres niveles de brillo y puerto USB integrado",
        "price": 32.00,
        "imageUrl": "https://web-pro-resources.s3.us-east-2.amazonaws.com/public/optimized-resources/product/ac7e58f0-5d56-4049-b0f7-a7b1b2f7a478/image/lampara-pescritorio-regulabletouch-silvernegro-luz-600x600.jpg",
        "stock": 20,
        "category": "Hogar",
    },
    {
        "name": "Organizador de Cocina",
        "description": "Set de organizadores apilables para especias y utensilios de cocina",
        "price": 18.75,
        "imageUrl": "https://d35y5t5rad2lom.cloudfront.net/images/upload/77253/card/660b4124140027.38290852.jpg",
        "stock": 35,
        "category": "Hogar",
    },
    {
        "name": "Balon de Futbol",
        "description": "Balon de futbol tamano 5 con costura termica y diseno profesional",
        "price": 35.00,
        "imageUrl": "https://supermaxi-225de.kxcdn.com/wp-content/uploads/2024/08/843956550058-1-1.png",
        "stock": 30,
        "category": "Deportes",
    },
    {
        "name": "Banda de Resistencia Set",
        "description": "Set de 5 bandas elasticas con diferentes niveles de resistencia para ejercicio",
        "price": 15.99,
        "imageUrl": "https://supermaxi-225de.kxcdn.com/wp-content/uploads/2024/08/715280718124-1-70.jpg",
        "stock": 50,
        "category": "Deportes",
    },
    {
        "name": "Cafe Molido Premium",
        "description": "Cafe de origen colombiano tostado medio con notas de chocolate y caramelo",
        "price": 12.50,
        "imageUrl": "https://supermaxi-225de.kxcdn.com/wp-content/uploads/2025/09/8000070012141-1-16.png",
        "stock": 60,
        "category": "Alimentacion",
    },
    {
        "name": "Mix de Frutos Secos",
        "description": "Mezcla de almendras, nueces, pistachos y arandanos deshidratados 500g",
        "price": 9.99,
        "imageUrl": "https://supermaxi-225de.kxcdn.com/wp-content/uploads/2025/06/7861042579519-1-18.jpg",
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
