-- Run prisma migrate deploy or prisma db push before this

SET work_mem = '64MB';


COPY public."User"(name, email)
FROM '/data/user.csv'
DELIMITER ';'
CSV HEADER;

COPY public."Card"("userId", title)
FROM '/data/card.csv'
DELIMITER ';'
CSV HEADER;

COPY public."Task"("cardId", description)
FROM '/data/task.csv'
DELIMITER ';'
CSV HEADER;
