from gensim.corpora import WikiCorpus
import jieba
from langconv import *


def convert_function():
    space = ' '
    i = 0
    l = []
    zhwiki_name = '/home/chenyiwei/Projects/NLP/Assignment1/dataset/zhwiki-20220520-pages-articles-multistream.xml.bz2'
    f = open('/home/chenyiwei/Projects/NLP/Assignment1/dataset/zhwiki.txt', 'w', encoding='utf-8')
    # wiki = WikiCorpus(zhwiki_name, lemmatize=False, dictionary={})  # 从xml文件中读出训练语料
    wiki = WikiCorpus(zhwiki_name, dictionary={})  # 从xml文件中读出训练语料
    for text in wiki.get_texts():
        for temp_sentence in text:
            temp_sentence = Converter('zh-hans').convert(temp_sentence)  # 繁体中文转为简体中文
            seg_list = list(jieba.cut(temp_sentence))  # 分词
            for temp_term in seg_list:
                l.append(temp_term)
        f.write(space.join(l) + '\n')
        l = []
        i = i + 1

        if (i % 200 == 0):
            print('Saved ' + str(i) + ' articles')
    f.close()


if __name__ == '__main__':
    convert_function()