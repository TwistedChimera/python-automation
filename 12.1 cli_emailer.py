#! Python3
'''
cli_emailer.py

    sends email using arguments

'''

import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox(service=Service(GeckoDriverManager(path = r".\\Drivers").install()))
browser.get('https://account.proton.me/login')


failtxt = 'failed to find {}'
passtxt = 'found {}'
wait = WebDriverWait(browser, 60)
try:
    username = wait.until(EC.element_to_be_clickable(By.ID, 'username'))
    print(passtxt.format('username'))
except:
    print(failtxt.format('username'))
