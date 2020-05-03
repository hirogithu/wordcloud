import argparse
import request_html

def txt_save(txt):
    with open("./abst.html", "a", encoding="utf-8") as f:
        print(txt, file=f)

def main(url, max_pages):

    txt = request_html.request_get_abst_list(url)
    txt_save(txt)

    for i in range(10, max_pages, 10):
        txt = request_html.request_get_abst_list(url+'&start='+str(i))
        txt_save(txt)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", default='https://scholar.google.com/scholar?cites=5469943753756181884&as_sdt=2005&sciodt=0,5&hl=ja', help="set URL")
    parser.add_argument("--max", type=int, default=30, help="set num of load page")
    args = parser.parse_args()

    main(url=args.u, max_pages=args.max)
