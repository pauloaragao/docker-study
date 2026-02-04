# Guia Completo de Docker - Documentação e Comandos

## 📦 Imagens Docker

### Construir uma imagem
Cria uma imagem Docker a partir de um Dockerfile no diretório atual.
```bash
docker build -t nome-imagem .
```
**Com arquivo Dockerfile específico:**
```bash
docker build -t nome-imagem -f caminho/Dockerfile .
```
**Com argumentos de build:**
```bash
docker build -t nome-imagem --build-arg VAR=valor .
```

### Adicionar tags a uma imagem
Permite versionar imagens e marcar a versão `latest`. Boa prática para manter histórico de versões.
```bash
# Criar uma nova tag para uma imagem existente
docker tag nome-imagem:v1 nome-imagem:latest

# Com registry
docker tag nome-imagem:v1 usuario_registry/nome-imagem:latest
```

### Listar imagens locais
```bash
docker images
```

### Remover imagem
```bash
docker rmi nome-imagem:tag
```

---

## 🔐 Docker Registry (Login e Push)

### Autenticar no Registry
Realiza login no Docker Hub ou registry privado para permitir push/pull de imagens.
```bash
# Docker Hub padrão
docker login

# Registry customizado com usuário
docker login -u usuario_registry

# Registry privado
docker login seu-registry.com
```

### Enviar imagem para registry
Faz upload da imagem local para o registry remoto.
```bash
docker push usuario_registry/nome-imagem:versao

# Exemplo
docker push pauloaragaodev/kube-news:latest
```

### Fazer download de imagem do registry
```bash
docker pull usuario_registry/nome-imagem:versao
```

---

## 🐳 Gerenciamento de Containers

### Listar containers em execução
```bash
docker ps
```

### Listar todos os containers (inclusive parados)
```bash
docker ps -a
```

### Remover um container específico
```bash
# Container parado
docker container rm nome-container

# Container em execução (força remoção)
docker container rm -f nome-container
```

### Remover todos os containers
```bash
# Remove apenas containers parados
docker container prune

# Remove todos (parados e em execução)
docker container rm -f $(docker container ls -qa)
```

### Visualizar logs de um container
```bash
docker logs nome-container

# Seguir logs em tempo real
docker logs -f nome-container

# Últimas 100 linhas
docker logs --tail 100 nome-container
```

### Executar comando dentro de um container em execução
```bash
docker exec nome-container comando

# Exemplo: acessar shell do container
docker exec -it nome-container /bin/bash
```

---

## 🧹 Limpeza do Sistema Docker

### Remover recursos não utilizados
Remove imagens, containers e redes que não estão em uso.
```bash
docker system prune

# Com confirmação automática
docker system prune -f

# Remove também volumes não utilizados
docker system prune -a --volumes
```

### Ver uso de espaço em disco
```bash
docker system df
```

### Inspecionar recursos
```bash
# Detalhes de um container
docker inspect nome-container

# Detalhes de uma imagem
docker inspect nome-imagem
```

---

## 📁 Volumes Docker

Volumes são mecanismos para persistir dados gerados ou utilizados por containers. Existem três tipos principais:

### Bind Mount
O container aponta diretamente para um diretório do FileSystem da máquina host.
- ✅ Ideal para desenvolvimento (hot reload)
- ❌ Não funciona bem em ambientes de produção compartilhados
```bash
docker run -v /caminho/local:/caminho/container nome-imagem
```

### Volume
Volume gerenciado pelo Docker, armazenado em `/var/lib/docker/volumes/`.
- ✅ Melhor portabilidade entre sistemas
- ✅ Mais seguro para produção
- ✅ Funciona em qualquer OS
```bash
docker volume create nome-volume
docker run -v nome-volume:/caminho/container nome-imagem
```

### tmpfs
Armazena dados apenas em memória RAM, melhora performance mas perde dados quando container reinicia.
- ✅ Ótimo para dados temporários
- ❌ Dados não persistem
```bash
docker run --tmpfs /caminho/temp nome-imagem
```

### Comandos de Volumes
```bash
# Listar volumes
docker volume ls

# Inspecionar um volume
docker volume inspect nome-volume

# Remover volume específico
docker volume rm nome-volume

# Remover volumes não utilizados
docker volume prune
```

---

## 🌐 Networks Docker

Quando você cria containers, eles precisam se comunicar. Docker oferece diferentes tipos de redes:

### Tipos de Redes
- **bridge**: Rede privada isolada (padrão)
- **host**: Usa a rede do host diretamente
- **none**: Sem conectividade de rede
- **overlay**: Para Docker Swarm/Kubernetes

### Listar Networks
```bash
docker network ls
```

### Inspecionar uma Network
Visualiza containers conectados e configurações de IP.
```bash
docker network inspect nome-network
```

### Criar rede bridge
```bash
docker network create nome-network
```

### Criar rede com CIDR Block específico
Útil quando você precisa controlar faixas de IP.
```bash
docker network create --subnet=10.0.0.0/16 --gateway=10.0.0.1 nome-network
```

### Conectar um container a uma rede
```bash
docker network connect nome-network nome-container
```

### Desconectar um container da rede
```bash
docker network disconnect nome-network nome-container
```

### Remover Networks
```bash
# Rede específica
docker network rm nome-network

# Networks não utilizadas
docker network prune

# Forçar remoção
docker network rm -f nome-network
```


---

## 🚀 Docker Compose

Docker Compose permite definir e executar múltiplos containers com um único comando usando um arquivo `compose.yaml`.

### Comandos Básicos

#### Up - Iniciar containers
```bash
# Iniciar em modo daemon (background)
docker compose up -d

# Com build automático
docker compose up -d --build

# Remover containers órfãos (não mais no compose.yaml)
docker compose up -d --remove-orphans

# Modo interativo (vê logs em tempo real)
docker compose up
```

#### Down - Parar e remover containers
```bash
docker compose down

# Também remove volumes
docker compose down -v
```

#### Stop - Pausar containers sem remover
```bash
docker compose stop

# Container específico
docker compose stop nome-servico
```

#### Start - Reiniciar containers parados
```bash
docker compose start

# Container específico
docker compose start nome-servico
```

#### Build - Construir imagens
```bash
# Construir todas as imagens
docker compose build

# Reconstruir sem cache
docker compose build --no-cache

# Construir serviço específico
docker compose build nome-servico
```

#### Logs
```bash
# Ver logs de todos os containers
docker compose logs

# Seguir logs em tempo real
docker compose logs -f

# Logs de container específico
docker compose logs nome-servico

# Últimas 50 linhas
docker compose logs --tail 50
```

#### Exec - Executar comando em container
```bash
# Listar arquivos no container
docker compose exec nome-servico ls

# Acessar shell do container
docker compose exec -it nome-servico /bin/bash

# Executar comando npm
docker compose exec nome-servico npm install
```

---

### Conceitos Avançados

#### Profiles
Permite criar perfis de execução para separar serviços por ambiente.

```yaml
services:
  web:
    image: nginx
    profiles: ["prod", "dev"]
  
  debug-tools:
    image: debug-tools
    profiles: ["dev"]
```

**Uso:**
```bash
# Executar apenas com profile dev
docker compose --profile dev up -d

# Múltiplos profiles
docker compose --profile dev --profile test up -d
```

#### Depends On
Define dependências entre serviços. O Docker Compose aguarda o serviço dependente estar "healthy" ou "started" antes de iniciar o outro.

```yaml
services:
  app:
    image: app
    depends_on:
      db:
        condition: service_healthy
  
  db:
    image: postgres
    healthcheck:
      test: ["CMD", "pg_isready"]
      interval: 10s
      timeout: 5s
      retries: 5
```

#### Extends
Permite reutilizar configurações de outro arquivo compose.

```yaml
services:
  web:
    extends:
      file: common.yaml
      service: base-web
    ports:
      - "8080:80"
```

#### Merge e Includes
Combina múltiplos arquivos compose:

```bash
docker compose -f compose.yaml -f compose.prod.yaml up -d
```

---

## 🔍 Troubleshooting Docker

### docker info
Exibe informações detalhadas do Docker daemon.
```bash
docker info
```

### docker events
Monitora eventos em tempo real do Docker.
```bash
# Últimas 2 horas
docker events --since 2h

# Apenas eventos de criação
docker events --filter type=container --filter action=create
```

### docker inspect
Obtém informações JSON detalhadas de um container, imagem ou rede.
```bash
# Container
docker inspect nome-container | jq .

# Obter IP específico
docker inspect nome-container | grep IPAddress

# Imagem
docker inspect nome-imagem
```

### docker top
Lista processos em execução dentro de um container.
```bash
docker top nome-container
```

### docker stats
Exibe uso de CPU, memória e rede em tempo real.
```bash
# Todos os containers
docker stats

# Container específico
docker stats nome-container

# Sem atualizar (snapshot)
docker stats --no-stream
```

### docker logs com filtros
```bash
# Últimas 100 linhas com timestamps
docker logs --tail 100 -t nome-container

# Seguir em tempo real
docker logs -f nome-container

# Com timestamps
docker logs -t nome-container

# Desde uma data específica
docker logs --since 2026-02-01 nome-container
```

---

## 💚 Healthchecks

Um healthcheck verifica periodicamente se o container está funcionando corretamente, permitindo que orquestradores (Docker Compose, Kubernetes) tomem ações automáticas em caso de falha.

### Healthcheck na linha de comando
Executa um teste direto ao criar o container.
```bash
docker container run -d \
  -p 8080:3000 \
  --health-cmd "curl -f https://localhost:3000/health" \
  --health-interval 10s \
  --health-timeout 5s \
  --health-start-period 30s \
  --health-retries 3 \
  pauloaragaodev/simulador-caos:v1
```

**Parâmetros:**
- `--health-cmd`: Comando a executar (deve retornar 0 para sucesso)
- `--health-interval`: Intervalo entre testes (padrão: 30s)
- `--health-timeout`: Tempo máximo para o teste responder (padrão: 30s)
- `--health-start-period`: Tempo de espera antes do primeiro teste (padrão: 0s)
- `--health-retries`: Falhas consecutivas antes de marcar como unhealthy (padrão: 3)

### Healthcheck no Docker Compose
Configura healthcheck para um serviço no compose.yaml:

```yaml
services:
  app:
    image: pauloaragaodev/simulador-caos:v1
    ports:
      - "8080:3000"
    healthcheck:
      test: ["CMD", "curl", "-f", "https://localhost:3000/health"]
      interval: 30s
      timeout: 5s
      retries: 5
      start_period: 30s
```

**Desabilitar healthcheck (se necessário):**
```yaml
healthcheck:
  disable: true
```

### Healthcheck no Dockerfile
Configura healthcheck diretamente na imagem Docker, aplicável a todos os containers criados desta imagem.

```dockerfile
FROM node:20-alpine

WORKDIR /app
COPY . .

EXPOSE 3000

# Instalar curl para o healthcheck
RUN apk add --no-cache curl

HEALTHCHECK --interval=10s \
            --timeout=5s \
            --start-period=30s \
            --retries=3 \
            CMD curl -f https://localhost:3000/health || exit 1

CMD ["node", "server.js"]
```

**Alternativa com script customizado:**
```dockerfile
# Criar script de health
RUN echo '#!/bin/sh\ncurl -f https://localhost:3000/health || exit 1' > /healthcheck.sh && \
    chmod +x /healthcheck.sh

HEALTHCHECK --interval=15s --timeout=5s --retries=3 CMD /healthcheck.sh
```

### Estados do Healthcheck
- **starting**: Container iniciando (dentro do `start_period`)
- **healthy**: Container respondendo ao healthcheck corretamente
- **unhealthy**: Container falhou no healthcheck

### Verificar status
```bash
# Ver status atual
docker inspect --format='{{.State.Health.Status}}' nome-container

# Ver detalhes completos
docker inspect nome-container | grep -A 10 Health
```


---

## 📋 Boas Práticas

✅ **Use volumes named** em produção em vez de bind mounts  
✅ **Sempre use tags específicas** nas imagens (não apenas `latest`)  
✅ **Configure healthchecks** para serviços críticos  
✅ **Use networks customizadas** para melhor isolamento  
✅ **Remova recursos não utilizados** regularmente com `docker system prune`  
✅ **Defina limites de memória e CPU** em production  
✅ **Use `.dockerignore`** para reduzir tamanho das imagens  
✅ **Rotacionalize logs** para evitar consumo de disco  

---

## 🆘 Erros Comuns

### "pull access denied"
**Causa:** Imagem não existe no registry ou você não tem acesso.  
**Solução:** Verifique o nome da imagem, faça `docker login` ou construa a imagem localmente com `docker build`.

### "Connection refused"
**Causa:** Serviço ainda não está pronto.  
**Solução:** Configure `depends_on` com `condition: service_healthy` e `healthcheck`.

### "No space left on device"
**Causa:** Disco cheio com containers/imagens não utilizados.  
**Solução:** Execute `docker system prune -a` para limpar tudo não utilizado.

