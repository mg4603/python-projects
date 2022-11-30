from selenium import webdriver
from logging import debug, DEBUG, info, INFO, basicConfig, disable

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(DEBUG)

def find_element_by_class(browser, class_name):
    browser.get('https://inventwithpython.com')
    try:
        elem = browser.find_element_by_class_name(class_name)
        info('Found <%s> element with that class name!' % elem.tag_name)
    except:
        info('Was not able to find an element with that name.')

def click_page(browser, text):
    browser.get('https://inventwithpython.com')
    try:
        link_elem = browser.find_element_by_link_text(text)
        link_elem.click()
    except:
        info('Was not able to find an element with that link text')

def main():
    browser = webdriver.Firefox()
    find_element_by_class(browser, 'cover-thumb')

if __name__ == '__main__':
    main()