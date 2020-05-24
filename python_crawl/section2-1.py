import urllib.request as req

img_url = 'https://cdn.mos.cms.futurecdn.net/otjbibjaAbiifyN9uVaZyL.jpg'
html_url = 'https://www.google.com/'

save_path1 = 'C:\W\cat.jpg'
save_path2 = 'C:\W\index.html'

try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('download failed')
    print('')
else:
    print('header1 >> ', header1)
    print('file1 >> ', file1)
    print('')
    print('header2 >> ', header2)
    print('file2 >> ', file2)
    print('download succeed')
