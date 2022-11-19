from requests import get
from bs4 import BeautifulSoup
from webbrowser import open
from sys import argv, exit
from pyperclip import paste

def parse_args():
    args = {}
    if len(argv) > 1:
        args['link'] = argv[1:]
    else:
        args['link'] = paste()
        if not args['link']:
            exit('Usage: link_extractor <url>\n\t<url>: url of page from which to extract links\n\tlink_extractor')
    return args
    
def main():
    args = parse_args()
    if args['link']:
        response = get(args['link'])
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a') if 'http' in link.get('href')]
        for link in links:
            open(link)

if __name__ == '__main__':
    main()