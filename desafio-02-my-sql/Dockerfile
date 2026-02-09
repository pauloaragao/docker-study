# MySQL Image for Development Environment
FROM mysql:8.0

# Metadados do container
LABEL maintainer="Dev Team" \
      description="MySQL" \
      version="1.0"

# Variáveis de ambiente para configuração do MySQL
ENV MYSQL_DATABASE=docker_db \
    MYSQL_USER=docker_usr \
    MYSQL_PASSWORD=docker_pwd \
    MYSQL_ROOT_PASSWORD=root_pwd

# Porta padrão do MySQL
EXPOSE 3306

# Volume para persistência de dados
VOLUME ["/var/lib/mysql"]

# Healthcheck para monitorar a saúde do container
HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=5 \
  CMD mysqladmin ping -u docker_usr -pdocker_pwd || exit 1
