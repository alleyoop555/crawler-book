
import codecs
import pyquery
import requests

def getProxy():
    response = requests.get('https://free-proxy-list.net')
    if response.status_code != 200:
        print('proxy page download: failed')
        return
    print('proxy page download: done')

    # with codecs.open('proxy.html', 'w', 'utf-8-sig') as f:
    #     f.write(response.text)

    proxies = []

    d = pyquery.PyQuery(response.text)
    table = d('table#proxylisttable')
    trs = table('tbody > tr')
    for tr in trs.items():
        ip = tr('td:nth-child(1)').text()
        port = tr('td:nth-child(2)').text()
        proxies.append({
            'ip': ip,
            'port': int(port)
        })
        # 以下為驗證 Proxy 是否可用的 Demo 程式碼
        # try:
        #     resp = requests.get(
        #         'https://www.google.com/',
        #         proxies={
        #             'https': f'https://{ip}:{port}'
        #         },
        #         timeout=3
        #     )
        #     print(resp.status_code)
        # except:
        #     pass

    return proxies

if __name__ == '__main__':
    print(getList())
