from bs4 import BeautifulSoup

html = '''
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <h1>This is h1 area.</h1>
        <h2>This is h2 area.</h2>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters.
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Laice</a>
            <a data-io="link3" href="http://example.com/little" class="brother" id="link3">Title</a>
        </p>
        <p class="story">
            story ...
        </p>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
# print('soup >> ', soup)
# print('type(soup) >> ', type(soup))
# print('soup.prettify() >> ', soup.prettify())

h1 = soup.html.body.h1
# print('h1 >> ', h1)
# print('h1.string >> ', h1.string)
p1 = soup.html.body.p
# print('p1 >> ', p1)
# print('p1.string >> ', p1.string)
p2 = p1.next_sibling.next_sibling
# print('p2 >> ', p2)
# print('dir(p2) >> ', dir(p2))
# print('p2.next_element >> ', p2.next_element)
# print('list(p2.next_element) >> ', list(p2.next_element))
p3 = p2.next_sibling.next_sibling
# print('p3 >> ', p3)

for v in p2.next_element:
    # print('v >> ', v)
    pass

soup2 = BeautifulSoup(html, 'html.parser')
link1 = soup.find_all('a', limit=2)
# print('link1 >> ', link1)
link2 = soup.find_all('a', class_='sister')
# link2 = soup.find_all('a', string=['Elsie', 'Title'])
# print('link2 >> ', link2)

for t in link2:
    # print('t >> ', t)
    pass

link3 = soup.find('a')
# print('link3 >> ', link3)
# print('link3.string >> ', link3.string)
# print('link3.text >> ', link3.text)
link4 = soup.find('a', {"class": "brother", "data-io": "link3"})
# print('link4 >> ', link4)

link5 = soup.select_one('p.title > b')
# print('link5 >> ', link5)
# print('link5.text >> ', link5.text)
# print('link5.string >> ', link5.string)
link6 = soup.select_one('a#link1')
# print('link6 >> ', link6)
# print('link6.string >> ', link6.string)
# print('link6.text >> ', link6.text)
link7 = soup.select_one('a[data-io="link3"]')
# print('link7 >> ', link7)
link8 = soup.select('p.story > a')
# print('link8 >> ', link8)
link9 = soup.select('p.story > a:nth-of-type(2)')
# print('link9 >> ', link9)

for t in soup.select('p.story'):
    temp = t.find_all('a')
    print('temp >> ', temp)

    if temp:
        for v in temp:
            # print('v >> ', v)
            print('v.string >> ', v.string)
    else:
        # print('t >> ', t)
        print('t.string >> ', t.string)
