# Task 5

# Use the BeautifulSoup and requests Python packages to print out a list of all the news titles on the https://news.ycombinator.com/.

# Constrain - single line statement

import requests
from bs4 import BeautifulSoup

def findTitle():
    #single line statement
    return [title.text for title in BeautifulSoup(requests.get("https://news.ycombinator.com/").text, 'html.parser').find_all('a', class_='storylink')]

print(findTitle())