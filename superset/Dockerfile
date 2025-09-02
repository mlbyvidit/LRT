FROM apache/superset:latest

USER root

RUN pip install psycopg2-binary

USER superset

# Set the default command for web service
CMD ["gunicorn", "-b", "0.0.0.0:8088", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info", "superset:app"]
