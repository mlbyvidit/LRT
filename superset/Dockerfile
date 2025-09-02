FROM apache/superset:latest

USER root

RUN pip install psycopg2-binary

USER superset

# Copy superset config
COPY --chown=superset:superset ../superset_config.py /app/pythonpath/superset_config.py

# Set environment variables
ENV SUPERSET_CONFIG_PATH=/app/pythonpath/superset_config.py
ENV FLASK_APP=superset

# Set the default command for web service
CMD ["gunicorn", "-b", "0.0.0.0:8088", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info", "--timeout", "120", "superset.app:create_app()"]
