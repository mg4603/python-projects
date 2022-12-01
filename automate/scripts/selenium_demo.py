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

def form_handler(browser, form_elem_id, form_elem_data):
    browser.get('https://login.metafilter.com')
    try:
        field_elem = browser.find_element_by_id(form_elem_id)
        field_elem.send_keys(form_elem_data)
    except:
        info('Was not able to find element with that elem_id')

def form_submitter(browser, form_elem_id):
    browser.get('https://google.com')
    try:
        field_elem = browser.find_element_by_id(form_elem_id)
        field_elem.submit()
    except:
        info('Was not able to find element with element id %s' % form_elem_id)

def main():
    browser = webdriver.Firefox()
    find_element_by_class(browser, 'cover-thumb')
    click_page(browser, 'Read Online for Free')

if __name__ == '__main__':
    main()