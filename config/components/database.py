from os import environ

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": environ.get("POSTGRES_DB"),
        "USER": environ.get("POSTGRES_USER"),
        "PASSWORD": environ.get("POSTGRES_PASSWORD"),
        "HOST": environ.get("SQL_HOST", "127.0.0.1"),
        "PORT": environ.get("SQL_PORT", 5432),
        "OPTIONS": {
            "options": environ.get("SQL_OPTIONS"),
        },
    }
}

CONTENT_SCHEMA = "content"
