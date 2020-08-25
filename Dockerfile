FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./backend/app/pyproject.toml ./backend/app/poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
ARG POSTGRES_DATABASE
ARG SERVER_HOST
ARG SERVER_NAME
ARG FIRST_SUPERUSER_PASSWORD
ARG POSTGRES_PASSWORD
ARG POSTGRES_SERVER
ARG POSTGRES_USER
ARG SECRET_KEY


RUN poetry install --no-root --no-dev

EXPOSE 80

COPY ./backend/app /app

#BACKEND
ENV PYTHONPATH=/app
ENV PROJECT_NAME=rock-keyword-history
ENV SERVER_NAME=$SERVER_NAME
ENV SERVER_HOST=$SERVER_HOST
ENV SECRET_KEY=$SECRET_KEY
ENV FIRST_SUPERUSER=rock.analytics@rockcontent.com
ENV FIRST_SUPERUSER_PASSWORD=$FIRST_SUPERUSER_PASSWORD
ENV SMTP_TLS=True
ENV SMTP_PORT=587
ENV SMTP_HOST=
ENV SMTP_USER=
ENV SMTP_PASSWORD=
ENV EMAILS_FROM_EMAIL=rock.analytics@rockcontent.com
ENV USERS_OPEN_REGISTRATION=False
ENV SENTRY_DSN=
# Postgres
ENV POSTGRES_SERVER=$POSTGRES_SERVER
ENV POSTGRES_USER=$POSTGRES_USER
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
ENV POSTGRES_DB=POSTGRES_DATABASE