from zipfile import ZipFile
import sys
from pathlib import Path
from os import walk

def find_latest_backup(folder_path, backup_path):
    folder_name = folder_path.stem
    number = 1
    while True:
        backup_name = '{}_{}.zip'.format(folder_name, str(number))
        if not (backup_path / backup_name).exists():
            return backup_name
        number += 1

def create_zip(folder_path, backup_path):
    with ZipFile(backup_path / find_latest_backup(folder_path, backup_path)) as backup_file:
        for foldername, subfolders, filenames in walk(folder_path):
            backup_file.write(foldername)

            for filename in filenames:
                new_base = folder_path.stem + '_'
                if filename.startswith(str(new_base)) and filename.endswith('.zip'):
                    continue
                backup_file.write(Path(foldername)/ filename)

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
    args = parse_args()
    folder_path = Path(args['folder_path'])
    backup_path = Path(args['backup_path'])
    create_zip(folder_path, backup_path)

if __name__ == '__main__':
    main()