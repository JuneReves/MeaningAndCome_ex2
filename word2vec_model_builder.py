#This should only be ran once to create the word2vec objects

import gensim
import pickle
from datetime import datetime

corpus = 'wackypedia_en1.words10.20Mwords'


def read_corp(corpus):
    sentences, cur_sent = list(), list()
    with open(corpus, 'r', errors='ignore') as f:
        sentences = []
        cur_sent = []
        for line in f.readlines():
            line = line.strip()
            if line == '</s>':
                sentences.append(cur_sent)
                cur_sent = []
            elif line == '<s>' or line.startswith('<text'):
                continue
            else:
                cur_sent.append(line)
    return sentences


s = datetime.now()
sentences = read_corp(corpus)
print('extracted sentences in ', (datetime.now() - s))

s = datetime.now()
with open('sentences_from_corp', 'wb') as output:
    pickle.dump(sentences, output, pickle.HIGHEST_PROTOCOL)

print('saved sentences in ', (datetime.now() - s))


def build_word2vec_object(min_appearences, window_size, dim,sentences):
        model = gensim.models.Word2Vec(sentences,min_count=min_appearences,window=window_size,size=dim)
        return model

s = datetime.now()

modelW10S100 = build_word2vec_object(5, 10, 100, sentences)
print('built model 10 100 in ', (datetime.now() - s))

s = datetime.now()

modelW2S100 = build_word2vec_object(5, 2, 100, sentences)
print('built model 2 100 in ', (datetime.now() - s))

s = datetime.now()

modelW10S1000 = build_word2vec_object(5, 10, 1000, sentences)
print('built model 10 1000 in ', (datetime.now() - s))

s = datetime.now()

modelW2S1000 = build_word2vec_object(5, 2, 1000, sentences)
print('built model 2 1000 in ', (datetime.now() - s))


outputfile = 'word2vec_models'
with open(outputfile, 'wb') as output:
    s = datetime.now()
    pickle.dump(modelW10S100, output, pickle.HIGHEST_PROTOCOL)
    print('saved model 10 100 in ', (datetime.now() - s))
    s = datetime.now()
    pickle.dump(modelW2S100, output, pickle.HIGHEST_PROTOCOL)
    print('saved model 2 100 in ', (datetime.now() - s))
    s = datetime.now()
    pickle.dump(modelW10S1000, output, pickle.HIGHEST_PROTOCOL)
    print('saved model 10 1000 in ', (datetime.now() - s))
    s = datetime.now()
    pickle.dump(modelW2S1000, output, pickle.HIGHEST_PROTOCOL)
    print('saved model 2 1000 in ', (datetime.now() - s))