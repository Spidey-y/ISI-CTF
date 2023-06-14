FROM python:3-alpine

RUN apk update && \
    apk add socat

COPY challenge /challenge/

WORKDIR /challenge

RUN chmod +x aa.py entrypoint.sh && adduser --disabled-password --no-create-home ctf && chown ctf aa.py
EXPOSE 1337
ENTRYPOINT ["./entrypoint.sh"]