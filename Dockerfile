FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY config ./config  

COPY project ./project

COPY scripts ./scripts

COPY manage.py ./

COPY Makefile ./

RUN make build

ENV DJANGO_SETTINGS_MODULE=config.settings.local

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]