# PostgreSQL Image for Development Environment
FROM postgres:18.1

# Metadados do container
LABEL maintainer="Dev Team" \
      description="PostgreSQL" \
      version="1.0"

# Variáveis de ambiente para configuração do PostgreSQL
ENV POSTGRES_DB=curso_docker \
    POSTGRES_USER=docker_usr \
    POSTGRES_PASSWORD=docker_pwd

# Porta padrão do PostgreSQL
EXPOSE 5432

# Volume para persistência de dados (opcional para desenvolvimento)
VOLUME ["/var/lib/postgresql"]

# Healthcheck para monitorar a saúde do container
HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=5 \
  CMD pg_isready -U docker_usr -d curso_docker || exit 1
