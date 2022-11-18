#!/usr/bin/env python3
from webbrowser import open
from urllib.parse import quote_plus
from sys import argv, exit
from pyperclip import paste
from logging import DEBUG, debug, basicConfig
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_args():
    args = {}
    if len(argv) > 1:
        args['search_terms'] = ' '.join(argv[1:])
    else:
        args['search_terms'] = paste()
        
        if not args['search_terms']:
            exit('Usage: web_search <search term>\n\t\t\t<search_term>: term to search(space separated)\n\tweb_search\twith term to search being on clipboard')
    return args

def main():
    args = parse_args()
    if args['search_terms']:
        url = 'https://www.google.com/search?q=%s'
        open(url % quote_plus(args['search_terms']))

if __name__ == '__main__':
    main()