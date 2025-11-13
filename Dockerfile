

FROM alpine:latest

RUN apk add --update --no-cache python3 py3-bottle
WORKDIR /app

COPY main.py .
COPY index.html .
COPY static/ ./static/

EXPOSE 5000
CMD ["python3", "main.py"]
