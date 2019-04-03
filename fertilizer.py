from bs4 import BeautifulSoup as bs
from urllib.request import (
    urlopen, urlparse, urlunparse, urlretrieve, urljoin)
import os
import sys

def extract(url):
    # Grab the episode page
    soup = bs(urlopen(url), features="lxml")

    #
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
            # print(episodes[-1])

    return episodes


def get_prerequisites(target_lesson_url, episode_data):

    soup = bs(urlopen(target_lesson_url), features="lxml")
    prerequisites = []

    for episode in episode_data:

        if episode["name"] in soup.text:
            print("Found", episode["name"], "in", target_lesson_url)

            prerequisites.append({"name": episode.name, "description": episode.name, "id": episode.url})

    if "for" in soup.text:
        prerequisites.append({"name": "lab", "description": "test", "id": "no url"})

    return prerequisites


def _usage():
    print("usage: python fertilizer.py")


if __name__ == "__main__":

    target_lesson = 'http://swcarpentry.github.io/python-novice-gapminder/13-looping-data-sets/index.html'

    urls = [
        'http://swcarpentry.github.io/shell-novice/reference/',
        'http://swcarpentry.github.io/git-novice/reference',
        'http://swcarpentry.github.io/python-novice-inflammation/reference',
        'http://swcarpentry.github.io/python-novice-gapminder/reference',
        'http://swcarpentry.github.io/r-novice-inflammation/reference',
        'http://swcarpentry.github.io/r-novice-gapminder/reference',    
    ]

    # Get all episodes from each lesson's reference page
    for url in urls:
        episode_list = extract_episode_urls(url)

    # Go through all the episodes and look for relevant keywords etc.
    # TODO: extract doesn't do anything useful yet!
    data_index = {}
    for episode in episode_list:
        episode["keywords"] = "test"

    # Work out which episodes are prerequisites for the target
    prerequisites = get_prerequisites(target_lesson, episode_list)

    print("Found the following prerequisites for lesson", target_lesson)
    print(prerequisites)
