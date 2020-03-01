import re
import requests
from bs4 import BeautifulSoup

occupation_class_ = {"soft":"rs", "hard":"rh", "design":"d", "sound":"s", "promotion":"k", "office":"j"}

def request_get_html_list(occupation):
    # スクレイピング対象の URL にリクエストを送り HTML を取得する
    res = requests.get('https://www.nintendo.co.jp/jobs/keyword/index.html')

    # レスポンスの HTML から BeautifulSoup オブジェクトを作る
    soup = BeautifulSoup(res.content, 'html.parser')

    icon_part = soup.find_all('ul', class_="keyword_list clearfix")
    for ul_tag in icon_part:

        links = [li.find('a').get('href') for li in ul_tag.find_all('li', class_="cat_" + occupation_class_[occupation])]
        print(links, len(links))
        break

#    links = [url.get('href') for url in soup.find_all('a')]
#    print(links, len(links))
    return links

def request_get_text(link):
    # スクレイピング対象の URL にリクエストを送り HTML を取得する
    res = requests.get('https://www.nintendo.co.jp/jobs/keyword/'+ link)

    # レスポンスの HTML から BeautifulSoup オブジェクトを作る
    soup = BeautifulSoup(res.content, 'html.parser')

    jdc_soup = soup.find_all("div", class_="jdc_txt")

    text_page = ""

    for jdc_soup_i in jdc_soup:

        jdc_soup_i.extract()

        #print(jdc_soup_i.get_text())

        text_page += jdc_soup_i.get_text()

    return text_page

def main(args):

    links = request_get_html_list(args.o)

    text = ""

    for link in links:

        if len(link) == 7:
            text += request_get_text(link)

    return text

