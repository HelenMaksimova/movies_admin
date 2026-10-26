from os import environ, path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = environ.get("SECRET_KEY")

DEBUG = environ.get("DEBUG") == "True"

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "[::1]"]
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

INTERNAL_IPS = ["127.0.0.1"]

STATIC_URL = "static/"
STATIC_ROOT = environ.get("STATIC_ROOT", path.join(BASE_DIR, "static"))

MEDIA_URL = "media/"
MEDIA_ROOT = environ.get("MEDIA_ROOT", path.join(BASE_DIR, "media"))

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
