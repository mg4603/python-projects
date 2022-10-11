from os.path import join, dirname
from app import create_app
from app.db import init_db, get_db
from pytest import fixture
from tempfile import mkstemp
from os import close, unlink

def get_data_sql(filename):
    with open(join(dirname(__file__), filename), 'rb') as f:
        _data_sql = f.read().decode('utf-8')
    
    return _data_sql


@fixture
def app():
    db_fd, db_path = mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(get_data_sql('data.sql'))
    
    yield app
    
    close(db_fd)
    unlink(db_path)

@fixture
def client(app):
    return app.test_client()

@fixture
def runner(app):
    return app.test_cli_runner()

class AuthActions:
    def __init__(self, client):
        self._client = client
    
    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username':username, 'password': password}
        )
    
    def logout(self):
        return self._client.get(
            '/auth/logout',
        )

@fixture
def auth(client):
    return AuthActions(client)