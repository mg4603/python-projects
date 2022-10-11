from pytest import fixture

@fixture
def app():
    app = create_app({
        'TESTING': True
    })
    
    yield app 
