from selenium import webdriver
from logging import debug, DEBUG, info, INFO, basicConfig, disable, exception

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(DEBUG)

def find_element_by_class(driver, class_name):
    driver.get('https://inventwithpython.com')
    try:
        elem = driver.find_element('class name', class_name)
        info('Found <%s> element with that class name!' % elem.tag_name)
    except:
        info('Was not able to find an element with that name.')

def click_page(driver, text):
    driver.get('https://inventwithpython.com')
    try:
        link_elem = driver.find_element('link text', text)
        link_elem.click()
    except Exception as e:
        exception(e)

# form handler for login.metafilter.com
def form_handler(driver, user_name, user_pass, url):
    driver.get(url)
    try:
        field_elem = driver.find_element('id', 'user_name')
        field_elem.send_keys(user_name)
        field_elem = driver.find_element('id', 'user_pass')
        field_elem.send_keys(user_pass)
        field_elem.submit()
    except Exception as e:
        exception(e)

def main():
    driver = webdriver.Firefox()
    find_element_by_class(driver, 'cover-thumb')
    click_page(driver, 'Read Online for Free')
    form_handler(driver, 'user_name', 'asdf', 'https://login.metafilter.com')

if __name__ == '__main__':
    main()