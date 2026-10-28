import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_celsius_to_fahrenheit_route(client):
    response = client.post('/convert', json={"celsius": 0})
    assert response.status_code == 200
    assert response.get_json()["fahrenheit"] == 32

    response = client.post('/convert', json={"celsius": 100})
    assert response.status_code == 200
    assert response.get_json()["fahrenheit"] == 212
