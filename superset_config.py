import os

# Superset specific config
ROW_LIMIT = 5000

# Flask App Builder configuration
# Your App secret key
SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY", "your_secret_key")

# The SQLAlchemy connection string
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@db:5432/lanesearch")

# Redis connection
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_URL': 'redis://redis:6379/0',
}

CELERY_CONFIG = {
    'broker_url': 'redis://redis:6379/0',
    'imports': ('superset.sql_lab',),
    'result_backend': 'redis://redis:6379/0',
    'worker_prefetch_multiplier': 1,
    'task_acks_late': False,
    'task_track_started': True,
}

# Enable embedded Superset dashboards
EMBEDDED_SUPERSET_ENABLED = True

# Feature flags
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
}
