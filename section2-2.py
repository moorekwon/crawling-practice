import urllib.request as req
from urllib.error import URLError, HTTPError



path_list = ['C:\W\lion.jpg', 'C:\W\index.html']

target_url = ['https://insp.ngo/wp-content/uploads/2019/07/BIA_The-Lion-King_1.jpg', 'https://www.google.com/']

for i, url in enumerate(target_url):
    try:
        response = req.urlopen(url)
        contents = response.read()
        print('------')
        print('header info-{}: {}'.format(i, response.info()))
        print('http status code: {}'.format(response.getcode()))
        print('------')

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print('download failed: httperror occured')
        print('e.code >> ', e.code)
    except URLError as e:
        print('download failed: urlerror occured')
        print('e.reason >> ', e.reason)
    else:
        print()
        print('download succeed')