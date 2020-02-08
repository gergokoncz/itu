# imports
import re
from nltk.corpus import stopwords

# variables
train_text = 'data/train.star.txt'
dev_star_text = 'data/dev.star.txt'
dev_star_other_text= 'data/dev.starOther.txt'
dev_other_text = 'data/train.star.txt'

word_list = []
word_set = set()
token_pattern = re.compile('[\(\)]|\[\'-\w]+|M[rs]\.|\.+|\w+')
m_sws = set(stopwords.words())

def convert_data(fp):
    with open(fp) as f:
        for l in f.readlines():
            tokens = token_pattern.findall(l)
            print(tokens)

if __name__ == '__main__':
    convert_data(train_text)
