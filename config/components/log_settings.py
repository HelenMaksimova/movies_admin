from logging import Filter, LogRecord
from os import getenv


class SQLLogFilter(Filter):
    def __init__(self):
        self.enabled = getenv("SQL_LOGGING", "True") == "True"
        super().__init__()

    def filter(self, record: LogRecord) -> bool:
        return self.enabled


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} "
            "{process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
        "sql": {
            "format": "[SQL] {sql}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "sql_log_filter": {
            "()": SQLLogFilter,
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "sql_console": {
            "level": "DEBUG",
            "filters": ["require_debug_true", "sql_log_filter"],
            "class": "logging.StreamHandler",
            "formatter": "sql",
        },
    },
    "loggers": {
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["sql_console"],  # Вывод SQL в консоль
            "propagate": False,
        },
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
