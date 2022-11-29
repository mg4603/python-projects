from selenium import webdriver
from logging import debug, DEBUG, info, INFO, basicConfig, disable

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(DEBUG)

def find_element(browser):
    browser.get('https://inventwithpython.com')
    try:
        elem = browser.find_element_by_class_name('cover-thumb')
        info('Found <%s> element with that class name!' % elem.tag_name)
    except:
        info('Was not able to find an element with that name.')

def main():
    browser = webdriver.Firefox()
    find_element(browser)

if __name__ == '__main__':
    main()