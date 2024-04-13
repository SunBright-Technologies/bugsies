FROM python:3.12 AS base

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

FROM base AS development

COPY requirements-dev.txt requirements-dev.txt
RUN python -m pip install -r requirements-dev.txt

WORKDIR /code
COPY ./bugsies /code/bugsies

CMD ["uvicorn", "bugsies.main:app", "--host", "0.0.0.0", "--port", "80"]
