FROM alpine



RUN apk update && apk add socat
COPY challenge /challenge/

WORKDIR /challenge
RUN chmod +x jail.sh entrypoint.sh && adduser --disabled-password --no-create-home ctf && chown ctf jail.sh
EXPOSE 1337
ENTRYPOINT ["./entrypoint.sh"]