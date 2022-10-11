from app import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.post(
        '/hello/form/',
        data={'greet': '', 'name': ''
    })
    assert response.headers['Location'] == '/hello/q%3Fgreet%3DHello%26name%3DNobody'
    