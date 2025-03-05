FROM postgres:14.17-bookworm

WORKDIR /data
COPY data ./

COPY copy.sql /docker-entrypoint-initdb.d/copy.sql