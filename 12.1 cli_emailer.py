#! Python3
'''
cli_emailer.py (wip)

    sends email using arguments

'''
# Logging
FORMAT='%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
# uncomment to disable log messages
logging.disable(logging.CRITICAL)

logging.debug('Start of program')

# House keeping
import traceback, shelve

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox(service=Service(GeckoDriverManager(path = r".\\Drivers").install()))

# Open email in browser
browser.get('https://account.proton.me/login')

# Explicitly wait 60 seconds
wait = WebDriverWait(browser, 60)

# Log-in
try:
    # wait until username textbox has height and width
    wait.until(EC.visibility_of_element_located((By.ID, 'username')))
    # grab email and password from file
    with shelve.open('userpass', 'c') as shelf:
        email = shelf['user']
        pw = shelf['pass']
    # grab email password textbox id
    email_elem = browser.find_element(By.ID, 'username')
    pw_elem = browser.find_element(By.ID, 'password')
    # enter email & password
    email_elem.send_keys(email)
    pw_elem.send_keys(pw)
    # submit form
    pw_elem.submit()
    # wait for password textbox to disappear
    wait.until(EC.staleness_of(pw_elem))
except:
    print(traceback.format_exc())

# Compose new message
try:
    # look for large button: 'new message' button)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button-large')))
    # once found, click button
    msg = browser.find_element(By.CSS_SELECTOR, '.button-large')
    msg.click()
    # wait focus to shift: 'To' textbox
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'field-focused')))
    # send keys to element in focus: 'To:' textbox)
    to_elem = browser.switch_to.active_element
    to_elem.send_keys('recepient_here')
    to_elem.send_keys(Keys.TAB)
    # wait until focus is shifted
    while to_elem == browser.switch_to.active_element:
        pass
    # write in subject
    subj_elem = browser.switch_to.active_element
    subj_elem.send_keys('subject_here')    
    
except:
    print(traceback.format_exc())

logging.debug('End of program')
