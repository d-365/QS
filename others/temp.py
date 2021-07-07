# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 15:41
# @Author  : dujun
# @File    : temp.py
# @describe:

if __name__ == '__main__':
    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.zhihu.com/explore'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html, 'lxml')
    data = soup.find_all(attrs={'class':'ExploreSpecialCard-title'})
    print(data)
    for i in range(len(data)):
        print(data[i].get_text())

