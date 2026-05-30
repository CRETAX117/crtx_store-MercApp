# CRTX Store - MercApp

## Datos del estudiante

| Campo | Detalle |
|-------|---------|
| **Nombre** | Brandon Cardenas |
| **Materia** | Aplicaciones Web |
| **Unidad** | 3 - Programacion del lado del cliente |
| **Grupo** | N1 |
| **Sede** | Cuenca |
| **GitHub** | https://github.com/CRETAX117/crtx_store-MercApp |

## Descripcion

Aplicacion web tipo catalogo de productos. Tiene un backend con Flask que expone una API REST y un frontend hecho con Vue 3 que consume esa API. Se pueden ver productos, buscar por nombre, filtrar por categoria, ver el detalle de cada uno, crear/editar/eliminar productos, y manejar un carrito de compras que se guarda en el navegador.

## Tecnologias

### Backend
- Python 3 con Flask
- PyMongo para la conexion a MongoDB
- Flask-CORS para permitir peticiones desde el frontend

### Frontend
- Vue 3 con Composition API y TypeScript
- Vite como herramienta de desarrollo
- Vue Router para la navegacion entre paginas
- Axios para las peticiones HTTP a la API

### Base de datos
- MongoDB

## Funcionalidades

- Catalogo de productos con busqueda por nombre y filtro por categoria
- Vista de detalle de producto con ruta dinamica
- CRUD completo: crear, editar y eliminar productos
- Carrito de compras con persistencia en localStorage
- Lazy loading de vistas con Suspense
- Diseno responsivo mobile-first
- API REST con validacion de datos y manejo de errores

## Estructura del proyecto

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
├── frontend/
│   ├── src/
│   │   ├── main.ts
│   │   ├── App.vue
│   │   ├── router/index.ts
│   │   ├── services/
│   │   ├── composables/
│   │   ├── types/
│   │   ├── views/
│   │   ├── components/
│   │   └── style.css
│   ├── package.json
│   └── vite.config.ts
├── README.md
├── readme.txt
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

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Se abre en http://localhost:5173

## Notas
- La base de datos ya esta configurada en el archivo .env
- Para la primera vez hay que ejecutar el seed para tener datos de prueba
- Revisar .env.example para ver las variables necesarias

## Despliegue

La app esta desplegada en:
- **Frontend:** _pendiente_ (Netlify)
- **API:** _pendiente_ (Railway)
- **Micrositio:** _pendiente_ (GitHub Pages)

La base de datos esta en MongoDB Atlas (cluster M0 gratuito).

### Variables de entorno para produccion

Backend (en Railway):
- `MONGO_URI` - URI de MongoDB Atlas
- `PORT` - lo asigna Railway solo
- `FRONTEND_URL` - URL de Netlify para CORS

Frontend (antes de hacer build):
- `VITE_API_URL` - URL de la API en Railway

