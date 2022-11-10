#! Python3
'''
cli_emailer.py (wip)

    sends email using arguments

'''
import logging

# Logging
FORMAT='%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
# uncomment to disable log messages
#logging.disable(logging.CRITICAL)
logging.disable(logging.DEBUG)

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
logging.info('opening browser')
browser.get('https://account.proton.me/login')

# Explicitly wait 60 seconds
wait = WebDriverWait(browser, 60)

# Log-in
try:
    # wait until username textbox has height and width
    logging.info('wait for page to load')
    wait.until(EC.visibility_of_element_located((By.ID, 'username')))
    # grab email and password from file
    logging.info('grad username and password')
    with shelve.open('userpass', 'c') as shelf:
        email = shelf['user']
        pw = shelf['pass']
    # grab email password textbox id
    logging.info('finding username')
    email_elem = browser.find_element(By.ID, 'username')
    logging.info('finding password')
    pw_elem = browser.find_element(By.ID, 'password')
    # enter email & password
    logging.info('typing email')
    email_elem.send_keys(email)
    logging.info('typing password')
    pw_elem.send_keys(pw)
    # submit form
    logging.info('submitting')
    pw_elem.submit()
    # wait for password textbox to disappear
    logging.info('waiting for page to disappear')
    wait.until(EC.staleness_of(pw_elem))
except:
    print(traceback.format_exc())

# Compose new message
try:
    # look for large button: 'new message' button)
    logging.info('wait for compose button')
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button-large')))
    # once found, click button
    logging.info('grab compose button')
    msg = browser.find_element(By.CSS_SELECTOR, '.button-large')
    logging.info('click compose')
    msg.click()
    # wait focus to shift: 'To' textbox
    logging.info('grab focused field')
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'field-focused')))
    to_elem = browser.switch_to.active_element
    # send keys to element in focus: 'To:' textbox)
    logging.info('enter recepient email')
    to_elem.send_keys('recepient_here')
    logging.info('pressed tab')
    to_elem.send_keys(Keys.TAB)
    # wait until focus is shifted
    logging.info('make sure focus is shifted')
    while to_elem == browser.switch_to.active_element:
        pass
    # write in subject
    logging.info('grab focused field')
    subj_elem = browser.switch_to.active_element
    logging.info('enter subject title')
    subj_elem.send_keys('subject_here')
    logging.info('pressed tab')
    browser.switch_to.active_element.send_keys(Keys.TAB)
    logging.info('pressed tab')
    browser.switch_to.active_element.send_keys(Keys.TAB)
    logging.info('type in editor')
    browser.switch_to.active_element.send_keys('bbbbbbbb sdf ksd ffjjdjd \n dfkjdjfkjfdjf')
    logging.info('sending email')
    webdriver.common.action_chains.ActionChains(browser)\
        .key_down(Keys.CONTROL)\
        .send_keys(Keys.ENTER)\
        .key_up(Keys.CONTROL)\
        .perform()
    
except:
    print(traceback.format_exc())

logging.debug('End of program')
