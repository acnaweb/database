# Database

Running databases in container

## Pre req

- Docker
    - [Docker](https://www.docker.com/)
    - [Docker/Playground](https://labs.play-with-docker.com/)
    - [Docker Hub](https://hub.docker.com/)
    - [Docker Cheatsheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)

## Databases

### Postgres

- https://hub.docker.com/_/postgres

```sh
docker run -d \
    -e POSTGRES_USER=new_user \
    -e POSTGRES_PASSWORD=my_pwd \
    -p 5432:5432 \
    postgres
```
### MySQL

- https://hub.docker.com/_/mysql

```sh
docker run -d \
    -e MYSQL_ROOT_PASSWORD=root_pwd \
    -e MYSQL_USER=new_user \
    -e MYSQL_PASSWORD=my_pwd \
    -p 3306:3306 \
    mysql
```

### SQL Server

- https://hub.docker.com/_/microsoft-mssql-server

> MSSQL_SA_PASSWORD -> 8 characters of at least three of these four categories: uppercase letters, lowercase letters, numbers and non-alphanumeric symbols

```sh
docker run -d \
    -e MSSQL_SA_PASSWORD=1q2w3e4R@ \
    -e "ACCEPT_EULA=Y" \
    -p 1433:1433 \
    mcr.microsoft.com/mssql/server:latest 
```

### Oracle

> - Oracle Account - Criar em https://www.oracle.com/

> - Selecionar a imagem no Registry da Oracle - https://container-registry.oracle.com/

* Efetuar login no Registry
  
```sh
docker login container-registry.oracle.com
```

* Pull da imagem
  
```sh
docker pull container-registry.oracle.com/database/free:latest
```
* Run

```sh
docker run -d \
    -e ORACLE_PWD=manager \
    -e ORACLE_CHARACTERSET=AL32UTF8 \
    -p 1521:1521 \
    -p 5500:5500 \
    oracle/database:23.3.0-free
```

### Redis

### MongoDB

> Info: Mongo Client https://www.mongodb.com/pt-br/products/tools/compass

- https://hub.docker.com/_/mongo

```sh
docker run -d \
    -e MONGO_INITDB_ROOT_USERNAME=mongo \
    -e MONGO_INITDB_ROOT_PASSWORD=root_pwd \
    -p 27017:27017 \
    mongo
```
## SQL Client

### DBeaver

- https://dbeaver.io/

### SQuirrel SQL

- https://squirrel-sql.sourceforge.io/

### SQL Developer/Oracle

- https://www.oracle.com/br/database/sqldeveloper/
