import pickle
import gensim.models.word2vec as word2vec
from simlexobj import simlexObj


with open('simlexObj', 'rb') as input:
    objList = pickle.load(input)

