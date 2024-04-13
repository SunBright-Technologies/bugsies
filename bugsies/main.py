from fastapi import FastAPI

from bugsies.models import SupportedFormat

app = FastAPI()


@app.get("/bugsie")
def get_bugsie() -> dict:
    return {"Hello": "World"}


@app.get("/bugsie/{version}")
def get_versioned_bugsie(version: str) -> dict:
    return {
        "Hello": "World",
        "version": version,
    }


@app.post("/bugsie")
def new_bugsie() -> dict:
    return {"Hello": "World"}


@app.post("/bugsie/{id}.{format}")
def new_bugsie_from_id_with_format(id: str, format: SupportedFormat) -> dict:
    return {
        "Hello": "World",
        "id": id,
        "format": format,
    }


@app.post("/bugsie/{id}")
def new_bugsie_from_id(id: str) -> dict:
    return {
        "Hello": "World",
        "id": id,
    }
