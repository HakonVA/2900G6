FROM python:3.8

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY config ./config  
COPY project ./project
COPY scripts ./scripts
COPY manage.py ./

RUN chmod +x scripts/*

RUN adduser -u 5678 --disabled-password --gecos "" user && \
    chown -R user /app
USER user

CMD ["scripts/entrypoint.sh"]