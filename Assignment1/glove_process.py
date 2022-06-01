import gensim
from gensim.test.utils import datapath, get_tmpfile
# from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

if __name__ == '__main__':
    # input file
    glove_file = datapath('/home/chenyiwei/Projects/NLP/Assignment1/glove/zhwiki_vectors.txt')
    # output file, binary = false
    tmp_file = get_tmpfile('/home/chenyiwei/Projects/NLP/Assignment1/model/zhwiki_glove_vectors.txt')
    glove2word2vec(glove_file, tmp_file)