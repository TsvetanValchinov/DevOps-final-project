import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test if the home page returns 200 OK and correct V2 message"""
    rv = client.get('/')
    assert rv.status_code == 200
    json_data = rv.get_json()

    assert json_data['message'] == "DevOps Final Project: V2"
    assert json_data['status'] == "Running on Kubernetes"
    assert json_data['maintenance_by'] == "GitHub Actions"


def test_health(client):
    """Test the health check endpoint"""
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.get_json()['status'] == "healthy"