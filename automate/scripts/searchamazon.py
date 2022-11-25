from logging import DEBUG, debug, CRITICAL, basicConfig, disable
from sys import argv, exit
from pyperclip import paste
from webbrowser import open
from requests import get
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def parse_args():
    args = {}
    if len(argv) > 1:
        args['product'] = ''.join(argv[1:])
    else:
        args['product'] = paste()
        if args['product'] == '':
            exit('Usage:\nsearchamazon <search_term>\n\t1. <search_term>: term to search for.\n\t2. Term to search for can be on clipboard')
    return args

def get_search_response(search_term):
    url = f'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={search_term}'
    debug('In get_search_response: %s' % url)
    response = get(url)
    try:
        response.raise_for_status()
    except Exception as e:
        debug('search error')
    debug('In get_search_response: %s' % response.status_code)
    return response

def get_links(response):
    pass

def main():
    args = parse_args()
    if args['product']:
        response = get_search_response(args['product'])
        links = get_links(response)
        debug(links)
        for link in links:
            open(f'https://amazon.in{link}')

if __name__ == '__main__':
    main()