import argparse

from wordcloud import WordCloud

from janome.tokenizer import Tokenizer

import request_html

def split_line(line):
    text = ''
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(line)
    for token in tokens:
        parts = token.part_of_speech.split(',')
        if (parts[0] == '名詞'):
            text = text + ' ' + token.surface
    return text

def main(args):
    line = request_html.main(args)
    text = split_line(line)

    wordcloud = WordCloud(background_color="white",
        font_path=r"C:\WINDOWS\Fonts\UDDigiKyokashoN-R.ttc",
        width=800,height=600).generate(text)

    wordcloud.to_file("./wordcloud_"+args.o+".png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", default="soft", help="set occupation ")
    args = parser.parse_args()
#    main(args)

    occupation_class_ = {"soft":"rs", "hard":"rh", "design":"d", "sound":"s", "promotion":"k", "office":"j"}
    for occupation in occupation_class_.keys():
        args.o = occupation
        main(args)