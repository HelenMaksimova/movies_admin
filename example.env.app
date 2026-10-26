PROJECT_NAME="Movie theater"
PROJECT_DESCRIPTION="The best movie theater for everyone"

DEBUG=True
SECRET_KEY=secret
SQL_LOGGING=False

PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1

DJANGO_SETTINGS_MODULE=config.settings
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin

STATIC_ROOT=/var/www/static/
MEDIA_ROOT=/var/www/media/

SQL_ENGINE=django.db.backends.postgresql_psycopg2
POSTGRES_USER=app
POSTGRES_PASSWORD=123qwe
POSTGRES_DB=theater

SQL_HOST=postgres
SQL_PORT=5432
SQL_OPTIONS=-c search_path=public,content
DATABASE_TYPE=postgres
