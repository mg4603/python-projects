from pytest import mark
from urllib.parse import quote_plus

@mark.parametrize(
    ('greet', 'name', 'response_str'),
    (
        ('test', 'test', 'Test, Test'),
    )
)
def test_hello(client, greet, name, response_str):
    assert b'Hello, Nobody' in client.get('/hello/').data
    response = client.get(quote_plus('/hello/q?greet=%s&name=%s' % (greet, name)))
    assert str.encode('%s'% response_str) in response.data

@mark.parametrize(
    ('greet', 'name', 'location'),
    (
        ('', '', 'q%3Fgreet%3DHello%26name%3DNobody'),
        ('test', '', 'q%3Fgreet%3Dtest%26name%3DNobody'),
        ('', 'test', 'q%3Fgreet%3DHello%26name%3Dtest'),
        ('test', 'test', 'q%3Fgreet%3Dtest%26name%3Dtest')
    )
)
def test_hello_form(client, greet, name, location):
    assert client.get('/hello/form/').status_code == 200
    response = client.post(
        '/hello/form/',
        data={'greet': greet, 'name': name
    })
    assert response.headers['Location'] == '/hello/%s'%location
