from flask import Blueprint, jsonify
from models import category as Category

categories_bp = Blueprint("categories", __name__)


@categories_bp.route("/", methods=["GET"])
def list_categories():
    categories = Category.get_all()
    return jsonify(categories)
