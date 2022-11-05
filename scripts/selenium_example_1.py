from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox(service=Service(GeckoDriverManager(path = r".\\Drivers").install()))
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element(By.CLASS_NAME, 'card-img-top')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
