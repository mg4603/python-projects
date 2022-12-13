from pathlib import Path

class HackingGame:
    GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

    def __init__(self, file_name):
        try:
            with Path(file_name).open('w') as file:
                self.WORDS = file.readlines()
            self.WORDS = [word.strip().upper() for word in self.WORDS]
        except FileNotFoundError:
            print('File {} not found in current working dir'.format(
                file_name
            ))