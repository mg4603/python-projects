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
from logging import debug, DEBUG, disable, CRITICAL, basicConfig, info, INFO
from pathlib import Path
from sys import argv, exit
basicConfig(level=INFO, format='%(asctime)s - %(levelName)s - %(message)s')
# disable(CRITICAL

def is_int(integer):
    try:
        int(integer)
        return True
    except:
        return False

def parse_args():
    args = {}
    if len(argv) > 1:
        args['number_of_strips'] = argv[1:]
        if not is_int(args['number_of_strips']):
            exit('Usage: python3 downloadXkcd.py <number>\n\t<number>: number of strips to download\n\t\t<number>: default - 50')
    else:
        args['number_of_strips'] = 50
    return args

def get_response_text(url):
    response = get(url)
    response.raise_for_status()
    return response.text

def get_img_prev_link(response_text):
    soup = BeautifulSoup(response_text, 'html.parser')
    img_link = soup.select('div#comic  img')
    if not img_link:
        exit('Comic image not found.')
    else:
        img_link = 'https:' + img_link
        prev_url = soup.select('a[rel="prev"]')[0]
        prev_url = 'https://xkcd.com' + prev_url.get('href')
    info('Done getting img and prev link')
    return img_link, prev_url

def get_comics(url, path, number_of_strips):
    while not url.endswith('#') and number_of_strips:
        info('Downloading page %s...' % url)
        response = get_response_text(url)
        img_link, url = get_img_prev_link(response)
        info('Downloading image %s...' % img_link)
        img = download_img(img_link)
        info('Saving image...')
        save(path, img)
        number_of_strips -= 1
    info('Done')

def main():
    args = parse_args()
    if args['number_of_strips']:
        url = 'https://xkcd.com'
        path = Path('../test_vals/xkcd')
        path.mkdir(parents=True, exist_ok=True)
        get_comics(url, path, args['number_of_strips'])

if __name__ == '__main__':
    main()