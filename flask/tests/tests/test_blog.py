from app.db import get_db
from pytest import mark

def test_index(client, auth):
    response = client.get('/')
    assert b'Log In' in response.data
    assert b'Register' in response.data

    auth.login()
    response = client.get('/') 
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data

@mark.parametrize(
    'path',
    (
        '/create/',
        '/1/update',
        '/1/delete',
    )
)
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers['Location'] == '/auth/login'

def test_author_required(app, client, auth):
    with app.app_context():
        db = get_db()
        db.execute(
            'UPDATE post SET author_id = 2 WHERE id = 1'
        )
        db.commit()
    
    auth.login()

    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403

    assert b'href="/1/update"' not in client.get('/').data