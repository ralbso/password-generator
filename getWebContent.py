"""
Created on Sun Apr  9 11:58:52 2017

@author: Raul
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

for h2 in soup.find_all(class_='story-heading'):
    print(h2.get_text().strip())
