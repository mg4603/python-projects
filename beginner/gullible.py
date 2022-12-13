class Gullible:
    def __init__(self):
        self.response = ''
    
    def display_intro(self):
        print('------------------------------------------------------------')
        print('------------------------- Gullible -------------------------')
        print('------------------------------------------------------------')
        print()
    
    def get_response(self):
        print('{}\n{}'.format(
            'Do you want to know how to keep a gullible', 
            'person busy for hours? (Y/N)'
        ))
        self.response = input('> ').strip().upper()
    
    def main(self):
        pass
