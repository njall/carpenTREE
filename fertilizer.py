from bs4 import BeautifulSoup as bs
from urllib.request import (
    urlopen, urlparse, urlunparse, urlretrieve)
import os
import sys

def extract(url):
    soup = bs(urlopen(url), features="lxml")
    parsed = list(urlparse(url))
    keyword_array = []
    for keyword in soup.findAll("dt"):
        keyword_array.append(keyword.text)
    return keyword_array

def _usage():
    print("usage: python fertilizer.py")

if __name__ == "__main__":
    urls = [
        'http://swcarpentry.github.io/shell-novice/reference/',
        'http://swcarpentry.github.io/git-novice/reference',
        'http://swcarpentry.github.io/python-novice-inflammation/reference',
        'http://swcarpentry.github.io/python-novice-gapminder/reference',
        'http://swcarpentry.github.io/r-novice-inflammation/reference',
        'http://swcarpentry.github.io/r-novice-gapminder/reference',    
    ]
    data_index = {}
    for url in urls:
        data_index[url] = extract(url)

    print(data_index)