import logging, re, pyperclip
import webbrowser, sys, requests
from bs4 import BeautifulSoup, NavigableString

# logging
FORMAT='%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
# disables log messages
#logging.disable(logging.CRITICAL)

logging.debug('Start of program')


# scraping
search_url = 'https://www.google.com/search?q='
search_query = ''

headers = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'
}


# initalize seach query: cli or args
if len(sys.argv) > 1:
    search_query = '%20'.join(sys.argv[1:])
else:
    search_query = input('search query: ')

# request url and get soup
res = requests.get(search_url + search_query)
res.raise_for_status() # raise exception on bad status
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# find the first 5 search results
#results = soup.select('a[href]')
results = soup.find_all('div', {'class': re.compile(r'(\w+[ ]?){3}')})
#pyperclip.copy(str(results))
for i in results:
    logging.info(i.find('a','href'))

#webbrowser.open(search_url + search_query)

logging.debug('End of program')
