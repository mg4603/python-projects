from sqlite3 import ProgrammingError
from app.db import get_db
from pytest import raises
from monkeypatch import setattr

def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with raises(ProgrammingError) as e:
        db.execute('SELECT 1')
    
    assert 'closed' in str(e.value)

def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False
    
    def fake_init_db():
        Recorder.called = True
    
    setattr('app.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called