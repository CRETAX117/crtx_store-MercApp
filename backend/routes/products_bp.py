from flask import Blueprint, jsonify, request
from models import product as Product

products_bp = Blueprint("products", __name__)


def validate_product(data, required=True):
    errors = []

    if required or "name" in data:
        name = data.get("name", "")
        if not name or not name.strip():
            errors.append("El nombre es obligatorio")
        elif len(name.strip()) < 3:
            errors.append("El nombre debe tener al menos 3 caracteres")

    if required or "price" in data:
        price = data.get("price")
        if price is None:
            errors.append("El precio es obligatorio")
        else:
            try:
                if float(price) <= 0:
                    errors.append("El precio debe ser mayor a 0")
            except (ValueError, TypeError):
                errors.append("El precio debe ser un numero valido")

    if required or "description" in data:
        desc = data.get("description", "")
        if not desc or not desc.strip():
            errors.append("La descripcion es obligatoria")

    if required or "categoryId" in data:
        cat_id = data.get("categoryId", "")
        if not cat_id:
            errors.append("La categoria es obligatoria")

    if "stock" in data:
        try:
            if int(data["stock"]) < 0:
                errors.append("El stock no puede ser negativo")
        except (ValueError, TypeError):
            errors.append("El stock debe ser un numero entero")

    return errors


@products_bp.route("/", methods=["GET"])
def list_products():
    search = request.args.get("search", "")
    category = request.args.get("category", "")
    products = Product.get_all(search=search or None, category=category or None)
    return jsonify(products)


@products_bp.route("/<product_id>", methods=["GET"])
def get_product(product_id):
    p = Product.get_by_id(product_id)
    if not p:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify(p)


@products_bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Se esperaba un JSON valido"}), 400

    errors = validate_product(data)
    if errors:
        return jsonify({"errors": errors}), 400

    product = Product.create(data)
    return jsonify(product), 201


@products_bp.route("/<product_id>", methods=["PUT"])
def update_product(product_id):
    existing = Product.get_by_id(product_id)
    if not existing:
        return jsonify({"error": "Producto no encontrado"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Se esperaba un JSON valido"}), 400

    errors = validate_product(data, required=False)
    if errors:
        return jsonify({"errors": errors}), 400

    updated = Product.update(product_id, data)
    return jsonify(updated)


@products_bp.route("/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    existing = Product.get_by_id(product_id)
    if not existing:
        return jsonify({"error": "Producto no encontrado"}), 404

    Product.delete(product_id)
    return jsonify({"message": "Producto eliminado"})
