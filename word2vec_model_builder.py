import gensim

corpus = 'wackypedia_en1.words10.20Mwords'

with open(corpus, 'r') as f:
    for l in f.readlines():
        print(l)

def build_word2vec_object(min_appearences, window_size, dim, corpus_filename):
    sentences, cur_sent = list(), list()
    with open(corpus_filename, 'r') as f:
        sentences = []
        cur_sent = []
        for line in f.readlines():
            print(line)
            line = line.strip()
            if line == '</s>':
                sentences.append(cur_sent)
                cur_sent = []
            elif line == '<s>' or line.startswith('<text'):
                continue
            else:
                cur_sent.append(line)
        print (sentences[0:10])
       # model = gensim.models.Word2Vec(sentences,min_count=min_appearences,window=window_size,size=dim)
       # return model

#print(build_word2vec_object(5,2,100,corpus))