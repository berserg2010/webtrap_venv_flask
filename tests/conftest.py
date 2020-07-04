import pytest

from main import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    app.app_context().push()
    yield app.test_client()


@pytest.fixture(params=["/", "/some-url"])
def get_url(request, client):
    def _get_url():
        return client.get(request.param)
    return _get_url()
