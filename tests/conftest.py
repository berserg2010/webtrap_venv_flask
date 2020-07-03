import pytest

from main import create_app


@pytest.fixture
def client():

    app = create_app({"TESTING": True})
    app.app_context().push()

    yield app.test_client()
