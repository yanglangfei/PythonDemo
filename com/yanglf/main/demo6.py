import requests
import json

url = 'https://www.sojson.com/auth_v_1_0/trash/complete.shtml'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.100 Safari/537.36',
    'origin': 'https://www.sojson.com',
    'referer': 'https://www.sojson.com/trash/18300492.htm',
    'authority': 'www.sojson.com'
}


def get_res():
    data = {
        'text': '石头'
    }
    res = requests.post(url, headers=headers, data=data)
    print(res.json())


if __name__ == '__main__':
    get_res()
