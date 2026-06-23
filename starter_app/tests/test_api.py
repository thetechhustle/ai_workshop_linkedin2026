import pytest
from fastapi.testclient import TestClient

from opportunity_tracker.app import app


@pytest.fixture()
def client(tmp_path, monkeypatch):
    db_path = tmp_path / "test.db"
    monkeypatch.setenv("OPPORTUNITY_DB_PATH", str(db_path))
    return TestClient(app)


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_and_list_opportunity(client):
    response = client.post(
        "/opportunities",
        json={"title": "Build portfolio", "source": "Workshop", "status": "idea"},
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Build portfolio"

    list_response = client.get("/opportunities")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1


def test_filter_and_update_status(client):
    created = client.post(
        "/opportunities",
        json={"title": "Practice demo", "source": "Career center", "status": "idea"},
    ).json()

    update_response = client.patch(
        f"/opportunities/{created['id']}/status",
        json={"status": "interview"},
    )
    assert update_response.status_code == 200
    assert update_response.json()["status"] == "interview"

    filtered_response = client.get("/opportunities?status=interview")
    assert len(filtered_response.json()) == 1


def test_missing_opportunity_returns_404(client):
    response = client.get("/opportunities/999")
    assert response.status_code == 404
