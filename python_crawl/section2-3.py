import requests
import lxml.html

def main():
    response = requests.get('https://www.naver.com/')
    urls = scrape_news_list_page(response)

    for url in urls:
        print('url >> ', url)

def scrape_news_list_page(response):
    urls = []

    # print('response.content >> ', response.content)
    root = lxml.html.fromstring(response.content)
    print('root >> ', root)

    for a in root.cssselect('.thumb_area .thumb_box .popup_wrap a.btn_popup'):
        url = a.get('href')
        if url == '#': pass
        else: urls.append(url)
    return urls

if __name__ == '__main__':
    main()

