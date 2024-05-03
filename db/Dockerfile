FROM ubuntu AS builder

RUN apt update && apt install -y wget
RUN wget "http://ergast.com/downloads/f1db.sql.gz"


FROM mysql
COPY --from=builder f1db.sql.gz /docker-entrypoint-initdb.d/

EXPOSE 3306
