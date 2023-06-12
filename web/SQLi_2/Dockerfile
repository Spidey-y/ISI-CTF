FROM python:3.9-alpine

WORKDIR /app
COPY challenge .
RUN pip install -r requirements.txt && adduser -D -u 1000 myuser && chown -R myuser:myuser /app
USER myuser
EXPOSE 1407
CMD ["flask","run","--host=0.0.0.0","--port=1407"]
