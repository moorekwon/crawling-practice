import urllib.request
from urllib.parse import urlparse

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url = 'http://www.encar.com'

mem = urllib.request.urlopen(url)

# print('type(mem) >> ', type(mem))
# print('mem.geturl() >> ', mem.geturl())
# print('mem.status >> ', mem.status)
# print('mem.getheaders() >> ', mem.getheaders())
# print('mem.getcode() >> ', mem.getcode())
# print("mem.read(200).decode('euc-kr') >> ", mem.read(200).decode('euc-kr'))
# print("urlparse('http://www.encar.com?id=moorekwon&pw=1111').query >> ", urlparse('http://www.encar.com?id=moorekwon&pw=1111').query)

API = 'https://api.ipify.org'

before_params = {
    'format': 'json'
}
print('before_params >> ', before_params)

after_params = urllib.parse.urlencode(before_params)
print('after_params >> ', after_params)

URL = API + '?' + after_params
print('URL >> ', URL)

data = urllib.request.urlopen(URL).read()
print('data >> ', data)

text = data.decode('utf-8')
print('text >> ', text)