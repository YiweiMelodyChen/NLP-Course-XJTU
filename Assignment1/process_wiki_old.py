from gensim.corpora import WikiCorpus
import os.path
import sys

# def convert_function():
#     space = ' '
#     i = 0
#     # l = []
#     wiki_name = './dataset/enwiki-latest-pages-articles.xml.bz2'
#     f = open('./dataset/enwiki2.txt', 'w', encoding='utf-8')
#     # wiki = WikiCorpus(zhwiki_name, lemmatize=False, dictionary={})  # 从xml文件中读出训练语料
#     wiki = WikiCorpus(wiki_name, dictionary={})  # 从xml文件中读出训练语料
#     for text in wiki.get_texts():
#         # for temp_sentence in text:
#         #     temp_sentence = Converter('zh-hans').convert(temp_sentence)  # 繁体中文转为简体中文
#         #     seg_list = list(jieba.cut(temp_sentence))  # 分词
#         #     for temp_term in seg_list:
#         #         l.append(temp_term)
#         f.write(space.join(decode_text(text)) + '\n')
#         # l = []
#         i = i + 1
#         if i % 1000 == 0:
#             print('Saved ' + str(i) + ' articles')
#     f.close()


def wiki_xml2txt_processing():
    i = 0
    input_file = "./dataset/enwiki-latest-pages-articles.xml.bz2"
    output_file = "./dataset/enwiki_data.txt"
    wiki = WikiCorpus(input_file, dictionary={})
    output = open(output_file, 'w', encoding="utf-8")
    for text in wiki.get_texts():
        str_line = " ".join(text) + "\n"
        output.write(str_line)
        i += 1
        if (i % 1000 ==0 ):
            print("Save "+str(i) + " articles")
    output.close()
    print("Finished saved " + str(i) + " articles")


if __name__ == '__main__':
    wiki_xml2txt_processing()