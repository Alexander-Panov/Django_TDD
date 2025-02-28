FROM python:slim

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src /src

WORKDIR /src

RUN python manage.py collectstatic --noinput

#RUN addgroup --system nonroot && adduser --system --group nonroot --shell /bin/sh
#
#USER nonroot

ENV DJANGO_DEBUG_FALSE=1
CMD gunicorn --bind :8888 TDD.wsgi:application