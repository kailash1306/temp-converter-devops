import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Temperature Converter Dashboard" in response.data

def test_celsius_to_fahrenheit_api(client):
    response = client.post('/convert/c-to-f', json={"celsius": 0})
    assert response.status_code == 200
    assert response.get_json()["fahrenheit"] == 32

    response = client.post('/convert/c-to-f', json={"celsius": 100})
    assert response.status_code == 200
    assert response.get_json()["fahrenheit"] == 212
