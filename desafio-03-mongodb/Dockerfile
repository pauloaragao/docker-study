# MongoDB Image for Development Environment
FROM mongo:7.0

# Metadados do container
LABEL maintainer="Dev Team" \
      description="MongoDB" \
      version="1.0"

# Porta padrão do MongoDB
EXPOSE 27017

# Volume para persistência de dados
VOLUME ["/data/db"]

# Healthcheck para monitorar a saúde do container
HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=5 \
  CMD mongosh --eval "db.adminCommand('ping')" || exit 1
