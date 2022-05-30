# NLP with Deep Learning -- XJTU

**Assignment 1**: Use word2vec and Glove to train distributed representation on the Intel computer, and compare their performance in **word clustering**. Analysis the compacts of relative corpus(like Pubmed) and general corpus(like Wikipedia) on the clustering.

[TOC]

## Introduction 

useful blog: https://zhuanlan.zhihu.com/p/56382372

differences between glove and word2vec and basic ideas about these two algorithms

## Dataset

### en-wiki

Wikipedia dataset dump https://dumps.wikimedia.org/enwiki/latest/

https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2 about 18.4G

put it under ./dataset folder

because the xml could not read directly, we should convert it into other format

followed by https://github.com/attardi/wikiextractor

```
git clone https://github.com/attardi/wikiextractor
python -m wikiextractor.WikiExtractor /home/chenyiwei/Projects/NLP/Assignment1/dataset/enwiki-latest-pages-articles.xml.bz2 -o /home/chenyiwei/Projects/NLP/Assignment1/dataset
```

this process takes about

9.52

## zh-wiki

https://dumps.wikimedia.org/zhwiki/20220520/zhwiki-20220520-pages-articles-multistream.xml.bz2 about 2.4G     put it under ./dataset folder

followed by https://github.com/skydark/nstools

```
git clone https://github.com/skydark/nstools
cd skydark/nstools
```

create data-transfer.py

```
python data-transfer.py
```

this process takes about 

9.10

### pubmed

Pubmed dataset dump https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/pubmed22n0001.xml.gz about 19M



## Word Vector Training

### Word2Vec

two model: CBOW & Skip-Gram

useful intro blog: https://guohongyi.com/2020/11/19/%E7%94%A8Python%E6%89%8B%E6%92%95word2vec/

useful repository: https://github.com/jind11/word2vec-on-wikipedia

useful method blog: https://blog.csdn.net/weixin_40547993/article/details/97781179

#### CBOW



#### Skip-Gram



### Glove

followed by https://nlp.stanford.edu/projects/glove/

```
$ git clone https://github.com/stanfordnlp/glove
$ cd glove && make
$ ./demo.sh
```



## Cluster

