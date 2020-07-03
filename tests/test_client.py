import pytest

from main import create_app


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_get_index(client):
    response = client.get('/')

    assert response.status_code == 200

    response = client.get('/some-url')

    assert response.status_code == 200
