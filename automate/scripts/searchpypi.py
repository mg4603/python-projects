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

def main():
    args = parse_args()
    if args['search']:
        links = get_links(args['search'])
        for link in links:
            open(link)

if __name__ == '__main__':
    main()