import re
import requests
from bs4 import BeautifulSoup

class Soup(object):
    def __init__(self, target_url):
        self.target_url = target_url

        # スクレイピング対象の URL にリクエストを送り HTML を取得する
        res = requests.get(self.target_url)

        # レスポンスの HTML から BeautifulSoup オブジェクトを作る
        self.soup = BeautifulSoup(res.content, 'html.parser')

    def get_titles(self):
        titles = []
        paper_titles = self.soup.find_all('h3', class_='gs_rt')
        for i, v in enumerate(paper_titles):
            titles.append(v.get_text())
            #print(i, titles[i])
        return titles

    def get_quoted_link(self):
        links = []
        paper_links = self.soup.find_all('h3', class_='gs_rt')
        for i, v in enumerate(paper_links):
            links.append(v.a.get('href'))
            #print(i, v.a.get('href'))
        return links, paper_links

    def get_part_of_abst(self):
        part_of_abst = []
        paper_abst = self.soup.find_all('div', class_='gs_rs')
        for i, v in enumerate(paper_abst):
            part_of_abst.append(v.get_text())
            #print(i, v.get_text())
        return part_of_abst

    def get_all_abst(self):
        abst_txt = ""
        _, paper_links = self.get_quoted_link()
        titles = self.get_titles()

        for i, v in enumerate(paper_links):
            link = v.a.get('href')
            res_i = requests.get(link)
            soup_i = BeautifulSoup(res_i.content, 'html.parser')
            absts = self.get_absts(soup_i)

            for abst in absts:
                txt = abst.get_text()
                abst_txt += "\n<paper>\n<title>" + titles[i] + "</title>"
                abst_txt += "\n<abst>" + txt + "</abst>\n</paper>\n"
                #print(txt[:20])

        return abst_txt

    @staticmethod
    def get_absts(soup_i):
        abst_re = re.compile('abstract*')
        # thecvf
        absts = soup_i.find_all(id=abst_re)
        if len(absts) > 0:
            return absts
        # nips, acm, arxiv
        absts = soup_i.find_all(class_=abst_re)
        return absts

def request_get_abst_list(target_url=""):

    soup_A = Soup(target_url)

    # show title
    #print(soup_A.get_titles())

    # show paper link, link_html
    #print(soup_A.get_quoted_link())

    # show abst
    #print(soup_A.get_part_of_abst())

    # show all abst
    abst_txt = soup_A.get_all_abst()

    return abst_txt

if __name__ == "__main__":

    target_url = 'https://scholar.google.com/scholar?cites=5469943753756181884&as_sdt=2005&sciodt=0,5&hl=ja'
    txt = request_get_abst_list(target_url)
    print(txt)
    for i in range(10, 30, 10):
        txt = request_get_abst_list(target_url+'&start='+str(i))
        print(txt)
