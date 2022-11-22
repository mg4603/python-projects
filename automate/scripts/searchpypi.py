'''
This is what your program does:
1. Gets search keywords from the command line arguments
2. Retrieves the search results page
3. Opens a browser tab for each result
This means your code will need to do the following:
1. Read the command line arguments from sys.argv.
2. Fetch the search result page with the requests module.
3. Find the links to each search result.
4. Call the webbrowser.open() function to open the web browser.
'''
from sys import argv, exit
from pyperclip import paste
from webbrowser import open
from requests import get

def parse_args():
    args = {}
    if len(argv) > 1:
        args['search'] = ' '.join(argv[1:])
    else:
        args['search'] = paste()
        if args['search'] == '':
            exit('Usage:\nsearchpypi <search_term>\n\t<search_term>: term to search for\n\tterm to search for in clipboard')
    return args

def get_search_response(search_term):
    url = 'https://google.com/search?q=%s'
    response = get(url % search_term)
    return response

def get_links(search_term):
    pass

def main():
    args = parse_args()
    if args['search']:
        response = get_search_response(args['search'])
        links = get_links(response)
        for link in links:
            open(link)

if __name__ == '__main__':
    main()