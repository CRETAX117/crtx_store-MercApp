import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/crtx_mercapp")
FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))
