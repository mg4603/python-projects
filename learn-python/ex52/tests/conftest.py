from pytest import fixture
from ..app import create_app

@fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    yield app