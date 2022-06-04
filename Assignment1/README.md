# NLP with Deep Learning -- XJTU

**Assignment 1**: Use word2vec and Glove to train distributed representation on the Intel computer, and compare their performance in **word clustering**. Analysis the compacts of relative corpus(like Pubmed) and general corpus(like Wikipedia) on the clustering.

[TOC]

## Introduction 

useful blog: https://zhuanlan.zhihu.com/p/56382372

differences between glove and word2vec and basic ideas about these two algorithms

## Dataset

### en-wiki

Wikipedia dataset dump website  

https://dumps.wikimedia.org/enwiki/latest/

https://dumps.wikimedia.org/enwiki/20220520/

download

https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2 about 18.4G

https://dumps.wikimedia.org/enwiki/20220520/enwiki-20220520-pages-articles-multistream1.xml-p1p41242.bz2 about 250MB

put it under ./dataset folder

because the xml could not read directly, we should convert it into other format

**try1** followed by https://github.com/attardi/wikiextractor

```
git clone https://github.com/attardi/wikiextractor
python -m wikiextractor.WikiExtractor /home/chenyiwei/Projects/NLP/Assignment1/dataset/enwiki-latest-pages-articles.xml.bz2 -o /home/chenyiwei/Projects/NLP/Assignment1/dataset
```

this way may have some bugs

**try2**  useful blog https://blog.csdn.net/Mr1060907970/article/details/54600629

```
python process_wiki.py
```

this process takes about hours to finish

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

this process takes about hours to finish

### pubmed

Pubmed dataset dump https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/pubmed22n0001.xml.gz about 19M

https://github.com/Franck-Dernoncourt/pubmed-rct/blob/master/PubMed_20k_RCT/train.txt

```
python process_pubmed.py
```



## Word Vector Training

### Word2Vec

two model: CBOW & Skip-Gram

useful intro blog: https://guohongyi.com/2020/11/19/%E7%94%A8Python%E6%89%8B%E6%92%95word2vec/

useful repository: https://github.com/jind11/word2vec-on-wikipedia

useful method blog: https://blog.csdn.net/weixin_40547993/article/details/97781179

#### CBOW

```
model = Word2Vec(LineSentence(wiki_news), sg=0, size=200, window=5, min_count=5, workers=6)
```

```
python train_w2v.py
```

#### Skip-Gram

```
model = Word2Vec(LineSentence(wiki_news), sg=1, size=200, window=5, min_count=5, workers=6)
```

```
python train_w2v.py
```

### Glove

followed by https://nlp.stanford.edu/projects/glove/

```
$ git clone https://github.com/stanfordnlp/glove
$ cd glove && make
$ ./demo.sh
```

modify demo.sh file and run

## Cluster

### choose words

cause the dataset is huge, in order to visualize the results, we choose the most frequent words in the dataset.

choose most frequent 500 words to do the cluster

```
python choose_word.py
```

### visualize cluster

TSNE + K-means

run the enwiki.ipynb, the visualized images can be found in the image folder

and to do the case, we choose 100 words from 5 classes 

when load glove model, should do extra process

```
python glove_process.py
```

the chinese may not be shown

followed by  https://blog.csdn.net/jeff_liu_sky_/article/details/54023745
