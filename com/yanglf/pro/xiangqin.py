import os

import requests
from bs4 import BeautifulSoup as bs
from aip import AipFace

url = 'http://www.xiangqinwang.cn/search_list.asp?Page={' \
      '}&kind=&age=&sheng=&shi=&quyu=&sex=Ů&submitok=b&ages=16&ages2=50&degree=&marriagestatus=&income=&shengao' \
      '=&hangye=&leixing=&s_order=0&keyname= '
APP_ID = '17070337'
APP_KEY = 'zrBSNcsWiE9KKBXs5G0sOaQS'
SECREY_KEY = '1m0V2Fe8nk8LF5WDFkDiBuZ9EC8VvwoW'
dir_path = '../xiangqin'
client = AipFace(APP_ID, APP_KEY, SECREY_KEY)
imageType = "BASE64"
options = {"face_field": "age,gender,beauty"}


def get_html(path):
    resp = requests.get(path)
    resp.encoding = resp.apparent_encoding
    return resp.text


def get_list(html):
    soup = bs(html, 'html.parser')
    lst = soup.find(class_='oe_userlist_layout').find_all('dl')
    mm = []
    for i in lst:
        user = {}
        head_face = i.find('dt').find('img')['src']
        nick_name = i.find('dd').find('h2').find('a').get_text()
        require = i.find('dd').find('h3').find('p').get_text()
        common = i.find('dd').find_all('p')
        user['head_face'] = 'http://www.xiangqinwang.cn/' + head_face
        user['nick_name'] = nick_name
        user['require'] = require
        mm.append(user)
    return mm


def download(i):
    face_url = i['head_face']
    tpe = face_url.split('.')[-1]
    nick_name = i['nick_name']
    face = requests.get(face_url)
    f = open(dir_path + '/' + nick_name + '.' + tpe, mode='wb')
    f.write(face.content)
    f.flush()
    f.close()


def get_yz_score(param):
    try:
        r = client.detect(param, imageType, options=options)
        print(r)
    except Exception:
        print('error')


def get_yanz():
    dir_lst = os.listdir(dir_path)
    res_lst = []
    for i in dir_lst:
        yanz = {'name': i.split('.')[0], 'score': get_yz_score(dir_path + "/" + str(i))}
        res_lst.append(yanz)


def main():
    for i in range(1, 2):
        path = url.format(str(i))
        html = get_html(path)
        mm = get_list(html)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for j in mm:
            download(j)
        print('download {} page'.format(str(i)))
    get_yanz()


if __name__ == '__main__':
    main()
