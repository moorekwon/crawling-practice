import json
import urllib.request as req
from fake_useragent import UserAgent


import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


ua = UserAgent()
# print('ua.ie >> ', ua.ie)
# print('ua.msie >> ', ua.msie)
# print('ua.chrome >> ', ua.chrome)
# print('ua.safari >> ', ua.safari)
# print('ua.random >> ', ua.random)

headers = {
    'User-agent': ua.ie,
    'referer': 'https://finance.daum.net/'
}

url = 'https://finance.daum.net/api/search/ranks?limit=10'

res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')
# print('res >> ', res)

rank_json = json.loads(res)['data']
# print('rank_json >> ', rank_json)

for elm in rank_json:
    # print('elm >> ', elm)
    print('순위: {}, 금액: {}, 회사명: {}'.format(elm['rank'], elm.get('tradePrice'), elm['name']))