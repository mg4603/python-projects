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
        while True:
            self.get_response()
            if self.response == 'Y' or self.response == 'YES':
                continue
            elif self.response == 'N' or self.response == 'NO':
                break
            else:
                print('{} is not a valid yes/no response.'.format(
                    self.response
                ))
        print('Thank you. Have a nice day!')


