import pytest

from main import create_app


def test_config():
    assert create_app("testing").testing


def test_get_index(get_url):
    assert get_url.status_code == 200
