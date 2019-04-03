from bs4 import BeautifulSoup as bs
from urllib.request import (
    urlopen, urlparse, urlunparse, urlretrieve, urljoin)
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

def extract_episode_urls(url):
    soup = bs(urlopen(url), features="lxml")
    episodes = []

    for table_row in soup.findAll("tr"):

        # See if this table row contains a link - if it is, it will go to an episode of this lesson
        link = table_row.find('a')
        if link:
            relative_url = table_row.find('a').get('href')
            absolute_url = urljoin(url, relative_url)
            episodes.append({"url": absolute_url, "name": link.text})
            print(episodes[-1])

    return episodes


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
        episode_list = extract_episode_urls(url)


    for episode in episode_list:
        data_index[url] = extract(url)


    # print(data_index)

    target_lesson = 'http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html'
    soup = bs(urlopen(target_lesson), features="lxml")

    prerequisites = []

    for lesson_url, episode_titles in data_index.items():
        for episode in episode_titles:
            if episode in soup.text:

                prerequisites.append({"name": episode, "description": episode, "id": lesson_url})


    print(prerequisites)

    # print(set(lesson_content))