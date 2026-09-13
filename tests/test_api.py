from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_agent_endpoint():
    response = client.get("/agent")

    assert response.status_code == 200

    body = response.json()

    assert body["agent_id"] == "soc-analyst-agent"
    assert body["status"] == "active"


def test_echo_endpoint():
    response = client.post(
        "/echo",
        json={"message": "Hello Zero Trust"},
    )

    assert response.status_code == 200

    body = response.json()

    assert body["received"] == "Hello Zero Trust"
    assert body["length"] == len("Hello Zero Trust")