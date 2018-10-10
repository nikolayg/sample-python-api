import pytest
from server.instance import server

@pytest.fixture
def app():
    app = server.app
    return app