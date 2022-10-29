from scripts.mad_libs import get_input, parse_args
import pyinputplus
import sys
from pytest import raises

def test_get_input(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(
            'pyinputplus.inputStr', 
            lambda prompt='Enter an adjective', blockRegexes='[a-zA-Z0-9]+ [a-zA-Z0-9]': 'asdf'
        )
        result = get_input('adjective')
    assert result == 'asdf'

def test_parse_args(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr('sys.argv', [])
        with raises(SystemExit) as pytest_wrapped_error:
            parse_args()
        assert pytest_wrapped_error.type == SystemExit

    with monkeypatch.context() as m:
        m.setattr('sys.argv', ['../scripts/mad_libs.py', 'in_path', 'out_path'])
        path_dict = parse_args()
    assert path_dict == {'in': 'in_path', 'out': 'out_path'}

    with monkeypatch.context() as m:
        m.setattr('sys.argv', ['../scripts/mad_libs.py', 'in_path'])
        path_dict = parse_args()
    assert path_dict == {'in': 'in_path'}