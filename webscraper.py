import requests
from bs4 import BeautifulSoup

URL = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"
r = requests.get(URL)

print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
print (soup.prettify())

title = soup.title.string
author = soup.find(rel="author").get_text()

print(title)
print(author)