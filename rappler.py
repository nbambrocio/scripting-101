import bs4
import requests
from lxml import etree
from bs4 import BeautifulSoup

URL = "https://www.rappler.com/topic/covid-19/"
page = requests.get(URL)

if page.status_code == 200:
    soup = bs4.BeautifulSoup(page.content, 'lxml')
    print(soup.prettify())
