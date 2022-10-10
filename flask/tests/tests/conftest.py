from os.path import join, dirname
from app import create_app
from app.db import init_db, get_db
from pytest import fixture
from tempfile import mkstemp

def get_data_sql(filename):
    with open(join(dirname(__file__), filename), 'rb') as f:
        _data_sql = f.read().decode('utf-8')
    
    return _data_sql
