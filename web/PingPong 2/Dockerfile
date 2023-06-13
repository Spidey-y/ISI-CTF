FROM python:3.9-alpine

WORKDIR /app
COPY challenge .
RUN pip install -r requirements.txt && apk add coreutils && adduser -D -u 1000 myuser && chown -R myuser:myuser /app && chmod 444 /app/flag.png && chmod 555 /app/app.py
USER myuser
EXPOSE 1417
CMD ["flask","run","--host=0.0.0.0","--port=1417"]
