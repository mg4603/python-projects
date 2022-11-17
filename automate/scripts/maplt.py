'''
This is what your program does:
1. Gets a street address from the command line arguments or clipboard
2. Opens the web browser to the Google Maps page for the address
This means your code will need to do the following:
1. Read the command line arguments from sys.argv.
2. Read the clipboard contents.
3. Call the webbrowser.open() function to open the web browser.
'''
from webbrowser import open
from urllib.parse import quote_plus
from pyperclip import paste
from sys import argv, exit

def parse_args():
    args = {}
    if len(argv) > 1:
        args['location'] = ' '.join(argv[1:])
    else:
        args['location'] = paste()
        if args['location'] == '':
            exit('Usage: maplt <location>\n\t<location> Location to search for as a command line args\n\t\t\t or copied to clipboard')
    return args

def main():
    args = parse_args()
    location = args['location']
    url = 'https://google.com/maps/search/' + quote_plus(location)
    open(url)

if __name__ == '__main__':
    main()

