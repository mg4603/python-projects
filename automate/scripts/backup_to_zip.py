from zipfile import ZipFile
import sys
from pathlib import Path

def find_latest_backup(folder_path, backup_path):
    folder_name = folder_path.stem
    number = 1
    while True:
        backup_name = '{}_{}.zip'.format(folder_name, str(number))
        if not (backup_path / backup_name).exists():
            break
        number += 1
    return backup_name

def create_zip(file_path):
    pass

def parse_args():
    args = {}
    if len(sys.argv) == 3:
        if Path(sys.argv[1]).exists():
            args['folder_path'] = sys.argv[1]
        else:
            exit('Given folder path doesn\'t exist')

        if Path(sys.argv[2]).is_dir():
            args['backup_path'] = sys.argv[2]
        else:
            exit('Given backup directory doesn\'t exist')
            
        return args
    exit(
        'usage: python3 <folder_path> <backup_path>\n\tfolder_path: path to folder to backup\n\tbackup_path: path to folder to store backup'
    )

def main():
    pass

if __name__ == '__main__':
    main()