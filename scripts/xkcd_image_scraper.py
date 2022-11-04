#! Python3
'''
xkcd_image_scraper

    downloads all xkcd comics
    skips existing downloads

    disclaimer:
    - all downloads are .jpg (naive implementation)
    - not robust, will end up with corrupted files

'''


import logging
import requests, re, os, sys
from bs4 import BeautifulSoup

FORMAT='%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='xkcd.log',level=logging.DEBUG, format=FORMAT)
# uncomment to disable log messages
#logging.disable(logging.CRITICAL)

logging.debug('Start of program')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 OPR/84.0.4316.14'
}

# create folder in current folder
folder_name = 'xkcd'
cwd = os.getcwd()
sep = os.sep
folder_path = cwd + sep + folder_name
txt = 'creating folder in: {}'
print(txt.format(folder_path))
# create folder if doesn't exist
if not os.path.isdir(folder_path):
    os.mkdir(folder_path)
# move inside created folder
os.chdir(folder_path)

# check folder for latest download (excluding gaps)
page = 1
while True:
    filename = str(page) + '.jpg'
    if not os.path.exists(filename):
        break
    else:
        logging.info(filename + ' exists, skipping . . .')
        print(filename + ' exists, skipping . . .')
    page += 1
logging.info('Starting at ' + filename)
print('Starting at ' + filename)
page = str(page)

# scrape
while True:
    try:
        # request page and get soup
        res = requests.get('https://xkcd.com/' + page, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.content, 'lxml')

        # search for image link
        imgURL = soup.find('a',{'href':re.compile(r'imgs.xkcd.com')})
        img = requests.get(imgURL['href'], headers=headers)

        # download image if doesn't exist
        file_name = page + '.jpg'
        if not os.path.isfile(file_name):
            file = open(file_name, 'wb')
            file.write(img.content)
            logging.info('Downloaded: ' + file_name)
            print('Downloaded: ' + file_name)
            file.close()
        else:
            logging.info('Skipping: ' + file_name)
            print('Skipping: ' + file_name)

        # check next page
        nextPageUrl = soup.find('a', {'rel':'next'})
        ## stop if last page
        if nextPageUrl['href'] == '#':
            logging.info('Last page, exiting. . . ')
            print('Last page, exiting . . .')
            break
        ## else grab next page number
        else:
            page = nextPageUrl['href'].strip('/')
            logging.info('Moving to next page: ' + page)
            print('Moving to next page: ' + page)
    except KeyboardInterrupt:
        # cleanly close and delete (presumably corrupted) file
        file = open(file_name, 'wb')
        file.close()
        os.unlink(file_name)
        print('Ctrl+c detected, exiting . . .')
        sys.exit()

logging.debug('End of program')

