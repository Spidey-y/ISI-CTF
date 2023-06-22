FROM python:3.9-alpine

RUN adduser -D myuser && mkdir /app
WORKDIR /app
COPY challenge .
RUN pip install -r requirements.txt && apk add coreutils
USER myuser
EXPOSE 1417
CMD ["flask","run","--host=0.0.0.0","--port=1417"]

