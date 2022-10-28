from scripts.mad_libs import get_input
import pyinputplus

def test_get_input(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr('pyinputplus.inputStr', lambda prompt='Enter an adjective': 'asdf')
        result = get_input('adjective')
    assert result == 'asdf'
    