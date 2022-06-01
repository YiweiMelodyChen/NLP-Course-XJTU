import re
import functools
import pandas as pd
import csv
import os, sys
import string


def pubmed_processing():
    # i = 0
    input_file = "./dataset/pubmed20k_train.txt"
    output_file = "./dataset/pubmed.txt"
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~]+'
    input = open(input_file, 'r', encoding="utf-8")
    output = open(output_file, 'w', encoding="utf-8")
    exp = ['OBJECTIVE', 'BACKGROUND', 'METHODS', 'RESULTS', 'CONCLUSIONS']
    for line in input.readlines():
        line = line.strip('\n')
        line = line.strip(string.digits)
        line = line.strip(string.punctuation)
        line = re.sub(r, ' ', line)
        line = line.rstrip(string.punctuation)
        for word in line.split():
            if word not in exp:
                str_line = "".join(word) + "\n"
                output.write(str_line)
    input.close()


    # wiki = WikiCorpus(input_file, dictionary={})
    # output = open(output_file, 'w', encoding="utf-8")
    # for text in wiki.get_texts():
    #     str_line = " ".join(text) + "\n"
    #     output.write(str_line)
    #     i += 1
    #     if (i % 1000 ==0 ):
    #         print("Save "+str(i) + " articles")
    # output.close()
    # print("Finished saved " + str(i) + " articles")


if __name__ == '__main__':
    pubmed_processing()