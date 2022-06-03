import argparse
import requests
import bs4
import lxml
from pytrends.request import TrendReq
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

author = config['author']['name']
author_github = config['author']['github']

print('Author name:', author)
print('Github:', github)

parser = argparse.ArgumentParser()
parser.add_argument('--source', help='reports/news/trends', default='reports' )
parser.add_argument('--date', help='date of data')
args = parser.parse_args()

if args.source == 'reports':
    pass

def parse_reports(date):
    # print('https://rapidapi.com/axisbits-axisbits-default/api/covid-19-statistics/')

    url = "https://covid-19-statistics.p.rapidapi.com/reports"

    querystring = {"iso":"PHL","date": date}

    headers = {
        "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com",
        "X-RapidAPI-Key": "ef1839b4f4mshf75e461ae429908p16ca68jsn1229d020f4d6"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def parse_news():
    
    url = "https://www.rappler.com/?s=covid"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    # print(soup.prettify())

    articles = soup.find_all('div', class_='archive-article__content')
    # print(articles)
    for article in articles:
        headline = article.find('h2')
        print(headline.text.strip())
       
        url = article.find('a')
        print(url.get('href'))

        date = article.find('time')
        print(date.text.strip())

def parse_trends():
    pytrends = TrendReq(hl='en-US', tz=360)
    df = pytrends.trending_searches(pn='philippines')
    print(df)

if args.source == 'reports':
    #validate input - 2022, convert to YYYY-MM-DD
    year = args.date.split('-')[0]
    if year == '2022':
        parse_reports(args.date)
    else:
        print('invalid year input')
elif args.source == 'news':
    parse_news()
elif args.source == 'trends':
    parse_trends()