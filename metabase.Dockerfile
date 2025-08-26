FROM metabase/metabase:v0.46.6

# Set environment variables
ENV MB_DB_TYPE=postgres
ENV MB_DB_DBNAME=lanesearch
ENV MB_DB_PORT=5432

# Set Java options for minimal memory usage
ENV JAVA_OPTS="-XX:+IgnoreUnrecognizedVMOptions -Dfile.encoding=UTF-8 -XX:+UseContainerSupport -XX:MaxRAMPercentage=40.0 -Xmx200m -Xms200m -XX:+UseG1GC -XX:MaxGCPauseMillis=200"

# Set Metabase specific options
ENV MB_ENCRYPTION_SECRET_KEY="deea10458acfbdc9f8633bf1d75794f2c01d935fa48660a2a7d25ac926f326a5"
ENV MB_ADMIN_EMAIL="mailshubhendu@zohomail.com"
ENV MB_ADMIN_PASSWORD="lanesearch123"

# Set Metabase to use minimal resources
ENV MB_ENABLE_EMBEDDING=true
ENV MB_ENABLE_PUBLIC_SHARING=true
ENV MB_ENABLE_ANALYTICS=false
ENV MB_ENABLE_TELEMETRY=false
ENV MB_ENABLE_SCHEDULING=false
ENV MB_ENABLE_EMAIL=false
ENV MB_ENABLE_SLACK=false
ENV MB_ENABLE_GOOGLE_AUTH=false
ENV MB_ENABLE_SAML=false
ENV MB_ENABLE_JWT=false

# Set host and port
ENV MB_SERVER_PORT=10000
ENV MB_SERVER_HOST=0.0.0.0

# Expose the port
EXPOSE 10000

# Start Metabase with health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5m --retries=3 \
    CMD curl -f http://localhost:10000/api/health || exit 1

# Start Metabase using the correct command
ENTRYPOINT ["/app/run_metabase.sh"] 