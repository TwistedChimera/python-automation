from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(service=Service(GeckoDriverManager(path = r".\\Drivers").install()))
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name(' cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
