# Para rodar local o Docker use o comando

docker container run -d -p 5432:5432 -e POSTGRES_PASSWORD=Pg123 -e POSTGRES_USER=kubenews -e POSTGRES_DB=kubenews -v kubenews_vol:/var/lib/postgresql/data postgres:14.10

# Para Rodar local
Se for a primeira vez que for rodar use 

$ npm install 



$ cd /home/pauloaragao/docker-study/projeto-exercicio && DB_DATABASE=kubedevnews DB_USERNAME=kubedevnews DB_PASSWORD=Pg123 node src/server.js
