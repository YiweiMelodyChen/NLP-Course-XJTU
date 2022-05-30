from gensim.models import Word2Vec
import gensim
from gensim.models.word2vec import LineSentence
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def train_w2v():
    wiki_news = open('./dataset/zhwiki.txt', 'r', encoding='utf-8')
    model = Word2Vec(LineSentence(wiki_news), sg=1, vector_size=200, window=5, min_count=5, workers=6, epochs=5)
    # sg=0 CBOW, sg=1 skip-gram
    # model.save('./model/zhwiki_cbow.word2vec')
    output_file = './zhwiki_sg_model'
    model.wv.save_word2vec_format(output_file, binary=False)


if __name__ == '__main__':
    train_w2v()
