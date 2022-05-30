# # -*- encoding:utf-8 -*-
# import logging
# import os.path
# import sys
# from gensim.corpora import WikiCorpus
#
# def decode_text(text):
#     words = []
#     for w in text:
#         words.append(w.decode('utf-8'))
#     return words
#
# if __name__ == '__main__':
#     program = os.path.basename(sys.argv[0])
#     logger = logging.getLogger(program)
#
#     logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
#     logging.root.setLevel(level=logging.INFO)
#     logger.info("running %s" % ' '.join(sys.argv))
#
#     # check and process input arguments
#     if len(sys.argv) < 3:
#         print(globals()['__doc__'] % locals())
#         sys.exit(1)
#     inp, outp = sys.argv[1:3]
#     space = " "
#     i = 0
#
#     output = open(outp, 'w')
#     # wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
#     wiki = WikiCorpus(inp, dictionary={})
#     for text in wiki.get_texts():
#         output.write(space.join(decode_text(text)) + "\n")
#         i = i + 1
#         if (i % 10000 == 0):
#             logger.info("Saved " + str(i) + " sentences")
#
#     output.close()
#     logger.info("Finished Saved " + str(i) + " sentences")

from gensim.corpora import WikiCorpus
import os.path
import sys



def wiki_xml2txt_processing():
    i = 0
    input_file = "./dataset/enwiki-20220520-pages-articles-multistream1.xml-p1p41242.bz2"
    output_file = "./dataset/enwiki-tiny.txt"
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