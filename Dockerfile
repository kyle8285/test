FROM python:3.7-alpine

WORKDIR /app

VOLUME /app/db

COPY frequent_browsers.py ./

RUN apk add sqlite

CMD ["python", "frequent_browsers.py"]
