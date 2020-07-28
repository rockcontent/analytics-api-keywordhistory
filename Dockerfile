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
RUN poetry install --no-root --no-dev

EXPOSE 80

COPY ./backend/app /app

#BACKEND
ENV PYTHONPATH=/app
ENV PROJECT_NAME=rock-keyword-history
ENV SERVER_NAME=localhost
ENV SERVER_HOST=http://localhost
ENV SECRET_KEY=q234adsfjasklj324123rsdfa975234sdgfkjahgsdfja
ENV FIRST_SUPERUSER=rock.analytics@rockcontent.com
ENV FIRST_SUPERUSER_PASSWORD=Slashdot!23
ENV SMTP_TLS=True
ENV SMTP_PORT=587
ENV SMTP_HOST=
ENV SMTP_USER=
ENV SMTP_PASSWORD=
ENV EMAILS_FROM_EMAIL=rock.analytics@rockcontent.com
ENV USERS_OPEN_REGISTRATION=False
ENV SENTRY_DSN=
# Postgres
ENV POSTGRES_SERVER=10.0.0.105
ENV POSTGRES_USER=tulio
ENV POSTGRES_PASSWORD=
ENV POSTGRES_DB=keyword_history