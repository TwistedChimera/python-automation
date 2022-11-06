#! Python3
'''
cli_emailer.py (wip)

    sends email using arguments

'''

import time, traceback

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox(service=Service(GeckoDriverManager(path = r".\\Drivers").install()))
browser.get('https://account.proton.me/login')

wait = WebDriverWait(browser, 60)
try:
    wait.until(EC.visibility_of_element_located((By.ID, 'username')))
    element = browser.find_element(By.ID, 'username')
    element.send_keys('asdf')
except:
    print(traceback.format_exc())
