from pytest import mark

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
    response = client.post(
        '/hello/form/',
        data={'greet': greet, 'name': name
    })
    assert response.headers['Location'] == '/hello/%s'%location
