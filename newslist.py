import codecs
from datetime import datetime
import os.path
import pyquery
import requests
import time
import urllib.parse as UP


def getList(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'web page download: fail')
    else:
        print(f'web page download: done')

    d = pyquery.PyQuery(response.text)
    posts = d('ul.vertical-list div.row')
    for post in posts.items():
       title = post('h3.title')
       link = title('a').attr('href')


if __name__ == "__main__":
    url = 'https://www.chinatimes.com/realtimenews/?chdtv'
    getList(url)