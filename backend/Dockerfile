FROM python:3.12-slim as build

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.lock

FROM python:3.12-slim

RUN groupadd -g 999 fastmock && useradd -r -u 999 -g fastmock fastmock

RUN mkdir /usr/app && chown fastmock:fastmock /usr/app
WORKDIR /usr/app

COPY --chown=fastmock:fastmock --from=build /usr/app/venv ./venv
COPY --chown=fastmock:fastmock . .
USER 999

ENV PATH="/usr/app/venv/bin:$PATH"
EXPOSE 8000


CMD ["fastapi", "run", "app/main.py"]
