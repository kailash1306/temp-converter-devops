import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_celsius_conversion(client):
    response = client.post('/', json={"celsius": 100})
    assert response.get_json()["fahrenheit"] == 212

def test_fahrenheit_conversion(client):
    response = client.post('/', json={"fahrenheit": 212})
    assert response.get_json()["celsius"] == 100
