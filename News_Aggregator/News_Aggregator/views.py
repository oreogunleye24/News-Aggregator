from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs4

soup = requests.get("https://www.washingtonpost.com/")

content = bs4(soup.content, 'html5lib')
headings = content.findAll("div", {"class": "headline relative gray-darkest pb-xs"})
wpnews = []
for span in headings:
    wpnews.append(span.text)

soup2 = requests.get("https://abcnews.go.com/")
content2 = bs4(soup2.content, 'html5lib')
headings2 = content2.findAll("div", {"class": "News__Content__Container"})
abcnews = []
for h2 in headings2:
    abcnews.append(h2.text)

def index(req):
    return render(req, 'news/index.html', {'wpnews': wpnews, 'abcnews': abcnews})

