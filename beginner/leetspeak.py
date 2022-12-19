'''
mapping
    'a': ['4', '@', '/-\\'],
    'c': ['('],
    'd': ['|)'],
    'e': ['3'],
    'f': ['ph'],
    'h': [']-[', '|-|'],
    'i': ['1', '!', '|'],
    'k': [']<'],
    'o': ['0'],
    's': ['$', '5'],
    't': ['7', '+'],
    'u': ['|_|'],
    'v': ['\\/']
'''

class LeetSpeak:
    def __init__(self, message):
        self.msg = message
    
    def main(self):
        leetspeak = self.english_to_leetspeak()
        print(leetspeak)

        try:
            copy(leetspeak)
            print('(Copied leetpeak to clipboard).')
        except NameError:
            pass