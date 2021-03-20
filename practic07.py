import requests
from bs4 import BeautifulSoup as bs

HOST = 'https://coinmarketcap.com/'
URL = 'https://coinmarketcap.com/'
HEADERS = {


           }
def get_html(url, params = ''):
    r = requests.get(url, headers = HEADERS, params=params)
    return r

html = get_html(URL)
soup = bs(html.text, 'lxml')
quotes = soup.find_all('td')
p = 0

for quote in quotes:

        print(quote.text)

#for quote in quotes:
#    if p < 8:
#        print(quote.text)
#    if p == 11:
#        p = 0
#    p += 1