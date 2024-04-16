from fastapi import FastAPI

from bugsies.models import SupportedFormat

app = FastAPI()

CURRENT_VERSION = "v1"
DEFAULT_FORMAT = SupportedFormat.SVG


@app.post("/bugsie")
def create_bugsie(seed: str | None = None) -> dict[str, str]:
    return create_versioned_bugsie(CURRENT_VERSION, seed)


@app.post("/bugsie/{version}")
def create_versioned_bugsie(version: str, seed: str | None = None) -> dict[str, str]:
    return {
        "message": "Placeholder: create bugsie",
        "version": version,
        "seed": seed or "",
    }


@app.get("/bugsie/{id}.{format}")
def get_bugsie_with_format(id: str, format: SupportedFormat) -> dict[str, str]:
    return {
        "message": "Placeholder: get bugsie",
        "id": id,
        "format": format,
    }


@app.get("/bugsie/{id}")
def get_bugsie(id: str) -> dict[str, str]:
    return get_bugsie_with_format(id, DEFAULT_FORMAT)
