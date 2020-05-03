import argparse

from cloudia import Cloudia
import config

def exclude_black_list(text):
    for word in config.BLACK_LIST:
        text = text.replace(word, "")
    return text

def main(args):

    with open(args.f, "r", encoding="utf-8") as f:
        text = f.read()
        text = exclude_black_list(text)

    Cloudia(text).save(fig_path=args.save_name, dark_theme=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", default="./abst.html", help="set file.")
    parser.add_argument("--save_name", default="./cloudia_abst.png", help="set file save name.")
    args = parser.parse_args()
    main(args)
