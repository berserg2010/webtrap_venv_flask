import pytest

from main import create_app, methods


@pytest.yield_fixture
def client():
    app = create_app("testing")
    app.app_context().push()
    yield app.test_client()


@pytest.fixture(params=methods)
def client_method(request, client):
    return getattr(client, request.param)


@pytest.fixture(params=["/", "/some-url", "/api", "/api/"])
def get_url(request, client_method):
    return client_method(request.param)

