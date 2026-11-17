FROM mysql:8.0
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=gait
COPY Init.sql /docker-entrypoint-initdb.d/
