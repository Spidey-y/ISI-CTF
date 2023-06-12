FROM python:3.9-alpine

WORKDIR /app
COPY challenge .
RUN pip install fastapi uvicorn && adduser -D -u 1000 myuser && chown -R myuser:myuser /app
USER myuser
EXPOSE 1405
CMD ["uvicorn","app:app","--host=0.0.0.0","--port=1405"]
