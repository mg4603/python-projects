from requests import get
from bs4 import BeautifulSoup
from webbrowser import open

def parse_args():
    pass

def main():
    args = parse_args()
    if args['link']:
        response = get(args['link'])
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]
        for link in links:
            open(link)

if __name__ == '__main__':
    main()