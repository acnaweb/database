# Database

Running databases in container

## Pre req

- Docker
    - [Docker](https://www.docker.com/)
    - [Docker/Playground](https://labs.play-with-docker.com/)
    - [Docker Hub](https://hub.docker.com/)
    - [Docker Cheatsheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)

## SQL Client

### DBeaver

- https://dbeaver.io/

### SQuirrel SQL

- https://squirrel-sql.sourceforge.io/


### SQL Developer/Oracle

- https://www.oracle.com/br/database/sqldeveloper/



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

- https://medium.com/xp-inc/dica-r%C3%A1pida-criando-base-de-dados-oracle-vers%C3%A3o-21-3-0-no-docker-357b05754b84


* Oracle Database 23c (23.3.0) Free
* Oracle Database 21c (21.3.0) Enterprise Edition, Standard Edition 2 and Express Edition (XE)
* Oracle Database 19c (19.3.0) Enterprise Edition and Standard Edition 2
* Oracle Database 18c (18.4.0) Express Edition (XE)
* Oracle Database 18c (18.3.0) Enterprise Edition and Standard Edition 2
* Oracle Database 12c Release 2 (12.2.0.2) Enterprise Edition and Standard Edition 2
* Oracle Database 12c Release 1 (12.1.0.2) Enterprise Edition and Standard Edition 2
* Oracle Database 11g Release 2 (11.2.0.2) Express Edition (XE)

 Parameters:
    -v: version to build
        Choose one of: 11.2.0.2  12.1.0.2  12.2.0.1  18.3.0  18.4.0  19.3.0  21.3.0 23.3.0
    -t: image_name:tag for the generated docker image
    -e: creates image based on 'Enterprise Edition'
    -s: creates image based on 'Standard Edition 2'
    -x: creates image based on 'Express Edition'
    -f: creates image based on Database 'Free'
    -i: ignores the MD5 checksums
    -p: creates and extends image using the patching extension
    -b: build base stage only (Used by extensions)
    -o: passes on container build option

```sh
git clone https://github.com/oracle/docker-images
cd docker-images/OracleDatabase/SingleInstance/dockerfiles
./buildContainerImage.sh -v 23.3.0 -f

```

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

