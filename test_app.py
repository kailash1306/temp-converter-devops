import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_loads(client):
    """Verifies that the simple JSON home page loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    # Checks for the word 'Online' in the status JSON instead of the old HTML dashboard name
    assert b"Online" in response.data

def test_celsius_to_fahrenheit_api(client):
    """Verifies the backend Celsius to Fahrenheit translation logic"""
    response = client.post('/convert/c-to-f', json={"celsius": 0})
    assert response.status_code == 200
    assert response.get_json()["fahrenheit"] == 32
