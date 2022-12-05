class CaesarHacker:
    def __init__(self):
        self.UPPER_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.LOWER_SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'

    def brute_force(self):
        pass

if __name__ == '__main__':
    print('Enter encrypted message to brute force.')
    encrypted_message = input('> ')
    cracker = CaesarHacker(encrypted_message)
    cracker.brute_force()