from pathlib import Path
import sys

from fastapi.testclient import TestClient


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app


client = TestClient(app)


def test_healthcheck_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Good Day": "Sunshine!"}