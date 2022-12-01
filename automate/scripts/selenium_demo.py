from selenium import webdriver
from logging import debug, DEBUG, info, INFO, basicConfig, disable, exception

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(DEBUG)

def find_element_by_class(driver, class_name):
    driver.get('https://inventwithpython.com')
    try:
        elem = driver.find_element_by_class_name(class_name)
        info('Found <%s> element with that class name!' % elem.tag_name)
    except:
        info('Was not able to find an element with that name.')

def click_page(driver, text):
    driver.get('https://inventwithpython.com')
    try:
        link_elem = driver.find_element_by_link_text(text)
        link_elem.click()
    except Exception as e:
        exception(e)

def form_handler(driver, form_elem_id, form_elem_data, url):
    driver.get(url)
    try:
        field_elem = driver.find_element_by_id(form_elem_id)
        field_elem.send_keys(form_elem_data)
    except:
        info('Was not able to find element with that elem_id')

def form_submitter(driver, form_elem_id, url):
    driver.get(url)
    try:
        field_elem = driver.find_element_by_id(form_elem_id)
        field_elem.submit()
    except:
        info('Was not able to find element with element id %s' % form_elem_id)

def main():
    driver = webdriver.Firefox()
    find_element_by_class(driver, 'cover-thumb')
    click_page(driver, 'Read Online for Free')

if __name__ == '__main__':
    main()