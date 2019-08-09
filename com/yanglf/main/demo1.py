import requests

url = "http://www.baidu.com"

# 开启 session 会话
s = requests.session()
# headers  头信息
headers = {
    "User-Agent": "Mozilla/5.0"
}
# params 参数
params = {
    "name": "张三",
    "age": 23
}
# files 上传文件
files = {
    'file': open('D:/bilibili/【灰白】听一只妖讲神的过去.flv', 'rb')
}
# data     post 请求数据
data = {
    "k": "v"
}
# form   form 表单
form = {
    "key1": [
        "value1",
        "value2"
    ]
}
# proxies 代理地址
proxies = {
    'http': 'http://177.130.55.164:20183',
    'https': 'https://177.130.55.164:20183'
}
# allow_redirects 是否重定向
# stream 是否下载文件  默认 true
# verify 是否  ssl 验证
# cert  证书

response = s.get(url, allow_redirects=False, stream=True)
# 如果状态码不是 200 抛出异常
response.raise_for_status()
# 响应信息头携带的编码 信息
encoding = response.encoding
print("encoding:{}".format(encoding))
# 从内容中 解析的编码
apparent_encoding = response.apparent_encoding
# 设置编码
response.encoding = response.apparent_encoding

print("apparent_encoding:{}".format(apparent_encoding))

# 二进制 字节流
content = response.content
print("content:{}".format(response.content))
# 文本内容
text = response.text
print("text:{}".format(response.text))
ru = response.url
h = response.headers
history = response.history
cookies = response.cookies
status = response.status_code
