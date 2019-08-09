import requests
from bs4 import BeautifulSoup as bs

url = "https://2.python-requests.org//zh_CN/latest/user/quickstart.html"
resp = requests.get(url)
resp.encoding = resp.apparent_encoding
soup = bs(resp.content, "html.parser")
sp = soup.prettify()
# TAG
title = soup.title
# parent
p = soup.title.parent
print(p)
