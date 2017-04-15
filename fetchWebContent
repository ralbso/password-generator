"""
Created on Sat Apr 15 16:00:57 2017

@author: Raul
"""

import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')
soup.prettify(formatter='html')

for paragraph in soup.find_all(class_='content-section'):
    print(paragraph.get_text())
