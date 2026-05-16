# CRTX Store - MercApp

## Datos del estudiante

| Campo | Detalle |
|-------|---------|
| **Nombre** | Brandon Cardenas |
| **Materia** | Aplicaciones Web |
| **Unidad** | 3 - Programacion del lado del cliente |
| **Grupo** | N1 |
| **Sede** | Cuenca |

## Descripcion

Aplicacion web tipo catalogo de productos. Tiene un backend con Flask que expone una API REST y un frontend con Vue 3 que consume esa API.

La idea es poder ver productos, buscarlos, filtrar por categoria, y manejar un carrito de compras.

## Tecnologias

### Backend
- Python 3 con Flask
- PyMongo para la conexion a MongoDB
- Flask-CORS para permitir peticiones desde el frontend

## Estructura

```
crtx_store-app/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── models/
│   │   ├── product.py
│   │   └── category.py
│   ├── routes/
│   │   ├── products_bp.py
│   │   └── categories_bp.py
│   └── seeds/
│       └── seed.py
├── README.md
├── .gitignore
└── .env.example
```

## Rutas de la API

| Metodo | Ruta | Que hace |
|--------|------|----------|
| GET | /api/products | Lista todos los productos (acepta ?search= y ?category=) |
| GET | /api/products/:id | Devuelve un producto por su ID |
| POST | /api/products | Crea un producto nuevo |
| PUT | /api/products/:id | Actualiza un producto existente |
| DELETE | /api/products/:id | Elimina un producto |
| GET | /api/categories | Lista todas las categorias |

## Como ejecutar

### Backend
```bash
cd backend
pip install -r requirements.txt
py seeds/seed.py
py app.py
```
El servidor se levanta en http://localhost:5000

## Notas
- Configurar las variables de entorno en backend/.env (ver .env.example)
- Ejecutar el seed la primera vez para tener datos de prueba
