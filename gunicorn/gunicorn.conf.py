bind = "0.0.0.0:8000"

workers = 4

threads = 8

enable_threads = True

timeout = 60
graceful_timeout = 10

max_requests = 5000
max_requests_jitter = 250

wsgi_app = "config.wsgi:application"

chdir = "/opt/app"

accesslog = "-"
errorlog = "-"
loglevel = "info"
