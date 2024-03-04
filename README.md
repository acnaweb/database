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

### Oracle



### SQL Server

### MongoDB

## References

- https://superuser.com/questions/816143/how-to-run-pip-in-non-interactive-mode
- https://docs.pytest.org/en/stable/reference/customize.html
- https://www.activestate.com/resources/quick-reads/how-to-manually-install-python-packages/
- https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
- https://serverspace.io/support/help/python-3-virtual-environment-on-ubuntu-22-04/

