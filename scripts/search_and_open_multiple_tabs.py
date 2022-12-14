import logging, re, time
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
res = requests.get(search_url + search_query, headers=headers)
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

logging.debug('Opening 5 urls')

# clean urls (links are surrounded with '&url=' and '&ved='
# change regex when necessary
urlRegex = re.compile(r'(?<=&url=).*(?=&ved=)')
# only open urls that isn't youtube
counter = 0;
for url in output:
    if not ('youtube.com' in url):
        logging.info(re.findall(urlRegex, url)[0])
        webbrowser.open(re.findall(urlRegex, url)[0])
        
        # only for the first 5 urls
        counter += 1
        if counter == 5:
            break

        # no need to sleep on last loop
        time.sleep(2)
        
logging.debug('End of program')
