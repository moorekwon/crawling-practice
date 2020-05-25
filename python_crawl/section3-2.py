import urllib.request
import urllib.parse

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


API = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'
params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# print('params >> ', params)

for c in params:
    # print('c >> ', c)
    param = urllib.parse.urlencode(c)
    # print('param >> ', param)
    url = API + '?' + param
    # print('url >> ', url)

    res_data = urllib.request.urlopen(url).read()
    # print('res_data >> ', res_data)
    contents = res_data.decode('utf-8')
    print('contents >> ', contents)
    print('------')