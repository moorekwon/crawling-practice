import requests
from lxml.html import fromstring, tostring

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def main():
    session = requests.Session()

    response = session.get('https://www.naver.com/')
    urls = scrape_news_list_page(response)
    # print('urls >> ', urls)

    for name, url in urls.items():
        print('name, url >> ', name, url)
    #     pass

def scrape_news_list_page(response):
    urls = {}
    # print('response.content >> ', response.content)
    root = fromstring(response.content)
    print('root >> ', root)
    for a in root.xpath('//div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]'):
        # print('a >> ', a)

        # print(tostring(a, pretty_print=True))
        # print()

        name, url = extract_contents(a)
        name = name
        urls[name] = url
    return urls

def extract_contents(dom):
    link = dom.xpath('./div[@class="popup_wrap"]/a[@class="btn_popup"]')[0].get('href')
    # print('link >> ', link)

    name = dom.xpath('./a[@class="thumb"]/img')[0].get('alt')
    # print('name >> ', name)
    return name, link

if __name__ == '__main__':
    main()

