from flask import Flask, jsonify
from flask_cors import CORS
from config import FLASK_PORT
from routes.products_bp import products_bp
from routes.categories_bp import categories_bp

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

app.register_blueprint(products_bp, url_prefix="/api/products")
app.register_blueprint(categories_bp, url_prefix="/api/categories")


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Recurso no encontrado"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Error interno del servidor"}), 500


if __name__ == "__main__":
    print(f"Servidor corriendo en http://localhost:{FLASK_PORT}")
    app.run(host="0.0.0.0", port=FLASK_PORT, debug=True)
