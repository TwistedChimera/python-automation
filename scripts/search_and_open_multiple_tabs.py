import logging, re, pyperclip, time
import webbrowser, sys, requests
from bs4 import BeautifulSoup

# logging
FORMAT='%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
# disables log messages
logging.disable(logging.CRITICAL)

logging.debug('Start of program')


# scraping
search_url = 'https://www.google.com/search?q='
search_query = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991'
}


# initalize seach query: cli or args
if len(sys.argv) > 1:
    search_query = '%20'.join(sys.argv[1:])
else:
    search_query = input('search query: ')

# request url and get soup
res = requests.get(search_url + search_query)
res.raise_for_status() # raise exception on bad status
soup = BeautifulSoup(res.content, 'lxml')

# find all search results
output = []
# the links are inside a div with a class with 3 words
results = soup.find_all('div', {'class': re.compile(r'^(\w+[ ]?){3}$')})
for item in results:
    # search the div for a div with a class with 4 words
    for item2 in item.find_all('div', {'class': re.compile(r'^(\w+[ ]?){4}$')}):
        # search for a link
        for item3 in item2.find_all('a', href=True):
            # if link has h3 (search result title), get the link
            for item4 in item3.find_all('h3', class_=True):
                logging.info(item3['href'])
                output.append(item3['href'])

# clean urls (links are surrounded with '/url?q=' and '&sa=U&ved='
# look behind and ahead for '/url?q=' and '&sa=U&ved=', respectively.
urlRegex = re.compile(r'(?<=\/url\?q=).*(?=&sa=U&ved=)')
# only open first 5 urls
for item in output[0:6]:
    # if url has /url?q= and isn't a youtube link
    if ('/url?q=' in item) and not ('youtube' in item):
        logging.info(re.findall(urlRegex, item)[0])
        webbrowser.open(re.findall(urlRegex, item)[0])
        time.sleep(1)
        
logging.debug('End of program')
