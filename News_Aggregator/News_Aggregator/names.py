import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, "html.parser")

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []
print("Times of India")
for th in toi_headings:
    toi_news.append(th.text)
print(toi_news)



#Getting news from theonion

ht_r = requests.get("https://www.theonion.com/")
ht_soup = BeautifulSoup(ht_r.content, "html.parser")
ht_headings = ht_soup.find_all('h4')
ht_headings = ht_headings[2:]
ht_news = []
print("The Onion News")
for hth in ht_headings:
    ht_news.append(hth.text)
print(ht_news)

