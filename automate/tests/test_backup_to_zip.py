from scripts.backup_to_zip import (
    parse_args, find_latest_backup
)
from pathlib import Path
from pytest import raises

def test_find_latest_backup():
    assert find_latest_backup(Path('./scripts'), Path('.')) == 'scripts_1.zip'

def test_parse_args(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr('sys.argv', ['./scripts/backup_to_zip.py'])
        with raises(SystemExit)  as sys_exit_err:
            parse_args()
        assert sys_exit_err.type == SystemExit
        assert str(sys_exit_err.value) \
            == \
            'usage: python3 <folder_path> <backup_path>\n\tfolder_path: path to folder to backup\n\tbackup_path: path to folder to store backup'
    with monkeypatch.context() as m:
        m.setattr('sys.argv', ['./scripts/backup_to_zip.py', '../scripts/asdf', '.'])
        with raises(SystemExit) as sys_exit_err:
            parse_args()
        assert sys_exit_err.type == SystemExit
        assert str(sys_exit_err.value)\
            == \
            'Given folder path doesn\'t exist'
    with monkeypatch.context() as m:
        m.setattr('sys.argv', ['./scripts/backup_to_zip.py', './scripts', '../asf'])
        with raises(SystemExit) as sys_exit_err:
            parse_args()
        assert sys_exit_err.type == SystemExit
        assert str(sys_exit_err.value)\
            ==\
            'Given backup directory doesn\'t exist'
    with monkeypatch.context() as m:
        m.setattr('sys.argv', ['./scripts/backup_to_zip.py', './scripts', './test_vals'])
        args = parse_args()
        assert args == {'folder_path': './scripts', 'backup_path': './test_vals'}