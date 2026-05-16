from models import db, ObjectId
import re

collection = db["products"]


def serialize(doc):
    if doc is None:
        return None
    doc["id"] = str(doc.pop("_id"))
    if "categoryId" in doc and isinstance(doc["categoryId"], ObjectId):
        doc["categoryId"] = str(doc["categoryId"])
    return doc


def get_all(search=None, category=None):
    query = {}

    if search:
        query["$or"] = [
            {"name": {"$regex": re.escape(search), "$options": "i"}},
            {"description": {"$regex": re.escape(search), "$options": "i"}},
        ]

    if category:
        try:
            query["categoryId"] = ObjectId(category)
        except Exception:
            pass

    docs = list(collection.find(query).sort("_id", -1))
    return [serialize(d) for d in docs]


def get_by_id(product_id):
    try:
        doc = collection.find_one({"_id": ObjectId(product_id)})
    except Exception:
        return None
    return serialize(doc)


def create(data):
    doc = {
        "name": data["name"].strip(),
        "description": data["description"].strip(),
        "price": float(data["price"]),
        "imageUrl": data.get("imageUrl", ""),
        "categoryId": ObjectId(data["categoryId"]),
        "stock": int(data.get("stock", 0)),
    }
    result = collection.insert_one(doc)
    doc["id"] = str(result.inserted_id)
    doc.pop("_id", None)
    doc["categoryId"] = str(doc["categoryId"])
    return doc


def update(product_id, data):
    try:
        oid = ObjectId(product_id)
    except Exception:
        return None

    updates = {}
    if "name" in data:
        updates["name"] = data["name"].strip()
    if "description" in data:
        updates["description"] = data["description"].strip()
    if "price" in data:
        updates["price"] = float(data["price"])
    if "imageUrl" in data:
        updates["imageUrl"] = data["imageUrl"]
    if "categoryId" in data:
        updates["categoryId"] = ObjectId(data["categoryId"])
    if "stock" in data:
        updates["stock"] = int(data["stock"])

    if not updates:
        return get_by_id(product_id)

    collection.update_one({"_id": oid}, {"$set": updates})
    return get_by_id(product_id)


def delete(product_id):
    try:
        oid = ObjectId(product_id)
    except Exception:
        return False
    result = collection.delete_one({"_id": oid})
    return result.deleted_count > 0
