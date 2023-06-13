FROM python:3.9-alpine

WORKDIR /app
COPY challenge .
RUN pip install flask && adduser -D -u 1000 myuser && chown -R myuser:myuser /app
USER myuser
EXPOSE 1401
CMD ["flask","run","--host=0.0.0.0","--port=1401"]
