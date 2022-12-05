'''
CaesarCipher:
    - intro
    - encrypt
    - decrypt
    - main 
'''
from pyperclip import copy

class CaesarCipher:
    def __init__(self):
        pass
    
    def intro(self):
        print('-------------------------Caesar Cipher-------------------------')
        print()

    def encrypt(self, msg):
        pass

    def decrypt(self, encrypted_msg):
        pass
    
    def main(self):
        while True:
            print('Do you want to (e)ncrypt or (d)ecrypt?')
            action = input('> ')
            action = action.lower().strip()
            if action.startswith('e') or action.startswith('d'):
                break
        
        while True:
            print('Please enter the key (0 to 25) to use.')
            key = input('> ')
            if key.isdecimal() and 0 <= int(key) <= 25:
                key = int(key)
                break
            
        if action.lower().strip().startswith('e'):
            print('Enter the message to encrypt')
            message = input('> ')
            encrypted_message = self.encrypt(key, message)
            print(encrypted_message)
            copy(encrypted_message)
            print('Full encrypted text copied to clipboard.')
        elif action.lower().strip().startswith('d'):
            print('Enter the message to decrypt')
            encrypted_message = input('> ')
            decrypted_message = self.decrypt(key, encrypted_message)
            print(decrypted_message)
            copy(decrypted_message)
            print('Full decrypted text copied to clipboard.')

if __name__ == '__main__':
    cipher = CaesarCipher()
    cipher.main()