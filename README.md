# Comandos Básicos para Docker

## Construir a imagem
```bash
docker build -t nome-imagem -f nome-dockerfile-usar .
```

## Logar no Container Registry
docker login or docker login -u user_registry

## Enviar imagem para registry
docker push user_registry/name_image:version

## Adicionar uma tag
É uma boa prática colocar tag da latest

docker tag  pauloaragaodev/kube-news:v1 pauloaragaodev/kube-news:latest

## Listar container rodando
docker ps 

## Remover todos os container de uma vez
docker container rm -f $(docker container ls -qa)

## Limpa tudo de docker no sistema 
docker system prune

# Volumes

## Bind 
O container aponta para pasta FileSystem para armazenamento. 

## Volume
Volume apontamento.

## tmpfs
Melhora a perfomace mapeando o arquivos porém não salva os dados. 



# Network
Quando voce cria um container com "docker run" ele já cria uma rede em bridge de forma automática em conjunto com a bridge principal. E com isso elas conseguem se comunicar entre os dois container. 

Existe tres tipos de redes padrão do container, sendo eles bridge, host e none. 

## Listar Networks
docker network ls

## Inspecionar Networks
docker network inspect id_network

## Criar rede network bridge
docker network create name_newtork

## Criar uma rede bridge indicando o CIRD Block de IP definido
Esse foco se precisar indicar manualmente para evitar possiveis problema ou seguir demanda técnica voce pode apontar os blocks de IPS.

docker network create --subnet=10.0.0.0/16 --gateway=10.0.0.1 outra_rede_docker

## Conectar um container da rede network
docker network connect nome_da_rede nome_do_container/id

## Desconectar um container da rede network
docker network disconnect nome_da_rede nome_do_container/id

## Remover networks manualmente
docker network rm -f id_network

## Remover em massa network que não são utilizados
docker network prune




# Docker compose

## Up

docker compose -f compose.yaml up -d

docker compose up -d


Para remover antigos que estejam no compose
docker compose up -d --remove-orphans


## down
docker compose down

## Stop
docker compose stop

## Start
docker compose start


## Build

docker compose build 