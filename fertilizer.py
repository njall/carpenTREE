from bs4 import BeautifulSoup as bs
from urllib.request import (
    urlopen, urlparse, urlunparse, urlretrieve)
import os
import sys

def extract(url):
    soup = bs(urlopen(url), features="lxml")
    keyword_array = []
    for keyword in soup.findAll("tr"):
        link = keyword.find('a')
        if (link):
            keyword_array.append(link.text)
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

    target_lesson = 'http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html'
    soup = bs(urlopen(target_lesson), features="lxml")
    prerequisite_lessons = []
    for lesson_url, lesson_content in data_index.items():
        for content in lesson_content:
            if content in soup.text:
                prerequisite_lessons.append(lesson_url)
    print(set(prerequisite_lessons))