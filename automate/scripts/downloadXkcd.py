'''
Here’s what your program does:
1. Loads the XKCD home page
2. Saves the comic image on that page
3. Follows the Previous Comic link
4. Repeats until it reaches the first comic
This means your code will need to do the following:
1. Download pages with the requests module.
2. Find the URL of the comic image for a page using Beautiful Soup.
3. Download and save the comic image to the hard drive with
iter_content().
4. Find the URL of the Previous Comic link, and repeat.
Open a new file editor tab and save it as downloadXkcd.py.
Step 1: Design the Program
If you open the browser’s developer tools and inspect the elements on the
page, you’ll find the following:
• The URL of the comic’s image file is given by the href attribute of an
<img> element.
• The <img> element is inside a <div id="comic"> element.
• The Prev button has a rel HTML attribute with the value prev.
• The first comic’s Prev button links to the https://xkcd.com/# URL,
indicating that there are no more previous pages.
'''
from bs4 import BeautifulSoup
from requests import get
from logging import debug, DEBUG, disable, CRITICAL, basicConfig
from pathlib import Path
from sys import argv, exit
basicConfig(level=DEBUG, format='%(asctime)s - %(levelName)s - %(message)s')
# disable(CRITICAL

def parse_args():
    args = {}
    if len(argv) > 1:
        args['number_of_strips'] = argv[1:]
        if not is_digit(args['number_of_strips']):
            exit('Usage: python3 downloadXkcd.py <number>\n\t<number>: number of strips to download\n\t\t<number>: default - 50')
    else:
        args['number_of_strips'] = 50
    return args

def get_comics(url, path, number_of_strips):
    pass

def main():
    args = parse_args()
    if args['number_of_strips']:
        url = 'https://xkcd.com'
        path = Path('../test_vals/xkcd')
        path.mkdir(parents=True, exist_ok=True)
        get_comics(url, path, args['number_of_strips'])

if __name__ == '__main__':
    main()