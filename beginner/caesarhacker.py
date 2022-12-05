class CaesarHacker:
    def __init__(self, encrypted_msg):
        self.UPPER_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.LOWER_SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
        self.encrypted_msg = encrypted_msg

    def brute_force(self):
        for key in range(0, 26):
            translated = ''
            for symbol in self.encrypted_msg:
                symbol_ord = ord(symbol)
                if 65 <= symbol_ord <= 90:
                    symbol_ord = (symbol_ord -  65 - key) % 26
                    translated += self.UPPER_SYMBOLS[symbol_ord]
                elif 97 <= symbol_ord <= 122:
                    symbol_ord = (symbol_ord - 97 - key) % 26
                    translated += self.LOWER_SYMBOLS[symbol_ord]
                else:
                    translated += symbol
            print(f'Key #{key}: {translated}')

if __name__ == '__main__':
    print('Enter encrypted message to brute force.')
    encrypted_message = input('> ')
    cracker = CaesarHacker(encrypted_message)
    cracker.brute_force()