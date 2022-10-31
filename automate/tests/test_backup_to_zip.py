from scripts.backup_to_zip import (
    parse_args, find_latest_backup
)
from pathlib import Path

def test_find_latest_backup():
    assert find_latest_backup(Path('./scripts'), Path('.')) == 'scripts_1.zip'

