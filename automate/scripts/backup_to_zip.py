from zipfile import ZipFile

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
    pass

def main():
    pass

if __name__ == '__main__':
    main()