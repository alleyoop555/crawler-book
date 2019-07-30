import codecs
import time

import pyquery
import requests
import urllib.parse as UP

import proxy


def connect(name, url, proxy):
    try:
        response = requests.get(url, proxies = {'https': f'https://{proxy["ip"]}:{proxy["port"]}'}, timeout = 3)
    except:
        print(f'{name} download: failed (exception)')
        return None
    if response.status_code != 200:
        print(f'{name} download: failed (status code not 200)')
        return None
    print(f'{name} download: done')

    return response


def getLink(url):
    proxyList = proxy.getProxy()

    for proxyItem in proxyList:
        print(f'use proxy {proxyItem["ip"]}:{proxyItem["port"]}')
        response = connect('本書介紹', url, proxyItem)
        if response is None:
            print('connection is invalid')
            continue
        print('connection is valid')
        
        break

def getList(url):
    proxyList = proxy.getProxy()

    for proxyItem in proxyList:
        print(f'use proxy {proxyItem["ip"]}:{proxyItem["port"]}')
        response = connect('銷售榜', url, proxyItem)
        if response is None:
            print('connection is invalid')
            continue
        print('connection is valid')

        d = pyquery.PyQuery(response.text)
        posts = d('ul.clearfix div.type02_bd-a')
        for post in posts.items():
            title = post('h4')
            link = title('a').attr('href')
            print('書名 : ', title.text())
            print('連結 : ', link)
            print('----------------------')  
            getLink(link)   

        break
    
    # 開 UTF-8 編碼文字檔案
    # with codecs.open('book.u.html', 'w', encoding='utf-8-sig') as f:
    #     # 寫入 UTF-8 字串
    #     f.write(response.text)

    # 開二進位檔案
    # with open('book.b.html', 'wb') as f:
    #     # 寫入二進位資料
    #     f.write(response.content)

    

        


if __name__ == "__main__":
    url = 'https://www.books.com.tw/web/sys_tdrntb/books/?loc=subject_004'
    getList(url)