import pickle
import gensim.models.word2vec as word2vec
from simlexobj import simlexObj

#for the csv we will write later
titles = 'Word1\tWord2\tPOS tag\tSimilarity score\n'

#open all the simlex objects
with open('simlexObj', 'rb') as input:
    objList = pickle.load(input)


with open('w2s100', 'rb') as input:
    model = pickle.load(input)

rows = [titles]

for i in range(len(objList)):
    try:
        sim = model.wv.similarity(objList[i].word1,objList[i].word2)
    except:
        sim = 0
    rows.append(str(objList[i].word1)+'\t'+str(objList[i].word2)+'\t'+str(objList[i].POS)+'\t'+str(sim)+'\n')

with open('size100_window2', 'w') as f:
    f.writelines(rows)


with open('w10s100', 'rb') as input:
    model = pickle.load(input)

rows = [titles]

for i in range(len(objList)):
    try:
        sim = model.wv.similarity(objList[i].word1,objList[i].word2)
    except:
        sim = 0
    rows.append(str(objList[i].word1)+'\t'+str(objList[i].word2)+'\t'+str(objList[i].POS)+'\t'+str(sim)+'\n')

with open('size100_window10', 'w') as f:
    f.writelines(rows)


with open('w2s1000', 'rb') as input:
    model = pickle.load(input)

rows = [titles]

for i in range(len(objList)):
    try:
        sim = model.wv.similarity(objList[i].word1,objList[i].word2)
    except:
        sim = 0
    rows.append(str(objList[i].word1)+'\t'+str(objList[i].word2)+'\t'+str(objList[i].POS)+'\t'+str(sim)+'\n')

with open('size1000_window2', 'w') as f:
    f.writelines(rows)


with open('w10s1000', 'rb') as input:
    model = pickle.load(input)

rows = [titles]

for i in range(len(objList)):
    try:
        sim = model.wv.similarity(objList[i].word1,objList[i].word2)
    except:
        sim = 0
    rows.append(str(objList[i].word1)+'\t'+str(objList[i].word2)+'\t'+str(objList[i].POS)+'\t'+str(sim)+'\n')

with open('size1000_window10', 'w') as f:
    f.writelines(rows)

