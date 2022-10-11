from sqlite3 import ProgrammingError
from app.db import get_db
from pytest import raises

def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with raises(ProgrammingError) as e:
        db.execute('SELECT 1')
    
    assert 'closed' in str(e.value)