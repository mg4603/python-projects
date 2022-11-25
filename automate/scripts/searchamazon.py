from logging import DEBUG, debug, CRITICAL, basicConfig, disable
from sys import argv, exit
from pyperclip import paste
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