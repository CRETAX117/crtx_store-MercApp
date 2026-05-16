from models import db, ObjectId

collection = db["categories"]


def get_all():
    cats = list(collection.find())
    for c in cats:
        c["id"] = str(c.pop("_id"))
    return cats


def get_by_id(cat_id):
    try:
        cat = collection.find_one({"_id": ObjectId(cat_id)})
    except Exception:
        return None
    if cat:
        cat["id"] = str(cat.pop("_id"))
    return cat
