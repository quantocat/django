FROM python:3.12.2-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

RUN apk update && \
    apk add --update --no-cache postgresql-dev gcc python3-dev musl-dev && \
    pip install --upgrade pip  && \
    pip install pip-tools

COPY ./requirements.in .
COPY ./requirements-dev.in .

RUN pip install --upgrade pip && \
    rm -f requirements*.txt && \
    pip-compile requirements.in && \
    pip-compile requirements-dev.in && \
    pip-sync requirements*.txt

# copy project
COPY . .

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]