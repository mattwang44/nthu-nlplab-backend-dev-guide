from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

class TestAPI():
    def test_get_counter(self):
        response = client.get("/counter")
        assert response.status_code == 200
        assert response.json() == {"count": 0}

    def test_post_counter(self):
        response = client.post("/counter", json={"num": "2"})
        assert response.status_code == 200
        assert response.json() == {"count": 2}