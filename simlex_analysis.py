import pickle
import gensim.models.word2vec as word2vec
from simlexobj import simlexObj
import csv

titles = ['word1', 'word2', 'POS', 'SimLex999', 'conc(w1)', 'conc(w2)', 'concQ', 'Assoc(USF)', 'SimAssoc333', 'SD(SimLex)', 'sim2W100S', 'sim10W100S', 'sim2W1000S', 'sim10W1000S']


with open('simlexObj', 'rb') as input:
    objList = pickle.load(input)

lst = [titles]
for w in objList:
    lst.append([
        w.word1,
        w.word2,
        w.POS,
        w.simlex999,
        w.concW1,
        w.concW2,
        w.concQ,
        w.assocUSF,
        w.simAssoc333,
        w.SDSimLex
    ])

similarities = []

with open('w2s100', 'rb') as input:
    modelW2S100 = pickle.load(input)

for i in range(len(objList)):
    try:
        sim = modelW2S100.wv.similarity(objList[i].word1,objList[i].word2)
    except:
        sim = 0
    try:
        similarities[i].append(sim)
    except:
        similarities.append([sim])

del(modelW2S100)



with open('w10s100', 'rb') as input:
    modelW10S100 = pickle.load(input)

for i in range(len(objList)):
    try:
        sim = modelW10S100.wv.similarity(objList[i].word1,objList[i].word2)
    except:
        sim = 0
    similarities[i].append(sim)

del(modelW10S100)



with open('w2s1000', 'rb') as input:
    modelW2S1000 = pickle.load(input)

for i in range(len(objList)):
    try:
        sim = modelW2S1000.wv.similarity(objList[i].word1,objList[i].word2)
    except:
        sim = 0
    similarities[i].append(sim)

del(modelW2S1000)


with open('w10s1000', 'rb') as input:
    modelW10S1000 = pickle.load(input)

for i in range(len(objList)):
    try:
        sim = modelW10S1000.wv.similarity(objList[i].word1,objList[i].word2)
    except:
        sim = 0
    similarities[i].append(sim)

del(modelW10S1000)

for i in range(len(lst)):
    if i == 0:
        continue
    lst[i] = lst[i] + similarities[i-1]


with open('all_data.csv', 'w') as f:
    wr = csv.writer(f, delimiter=',')
    for l in lst:
        wr.writerow(l)