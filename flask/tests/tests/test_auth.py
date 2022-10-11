from flask import g, session
from app.db import get_db
from pytest import mark

def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers['Location'] == '/auth/login'

    with app.app_context():
        assert get_db().execute(
            'SELECT * FROM user WHERE username=\'a\''
        ).fetchone() is not None

@mark.parametrize(
    ('username', 'password', 'message'),
    (
        ('', '', b'Username and password required'),
        ('a', '', b'Username and password required'),
        ('', 'a', b'Username and password required'),
        ('test', 'test', b'already exists.'),
    )
)
def test_register_validate(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data