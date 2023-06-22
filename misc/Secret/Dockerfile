FROM python:3-alpine

RUN apk update && \
    apk add socat

COPY challenge /challenge/

WORKDIR /challenge

RUN chmod +x challl.py entrypoint.sh && adduser --disabled-password --no-create-home ctf && chown ctf /challenge/*
EXPOSE 1337
ENTRYPOINT ["./entrypoint.sh"]