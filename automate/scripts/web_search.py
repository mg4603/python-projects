from webbrowser import open
from urllib.parse import quote_plus

def parse_args():
    pass

def main():
    args = parse_args()
    if args['search_terms']:
        url = 'https://www.google.com/search?q=%s'
        open(url % quote_plus(args['search_term']))

if __name__ == '__main__':
    main()