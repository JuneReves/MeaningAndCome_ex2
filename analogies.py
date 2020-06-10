import pickle
import gensim.models.word2vec as word2vec

with open('w2s100', 'rb') as input:
    model = pickle.load(input)


print('model w2 s100')
print('sun is to _ as black is to white:')
print(model.wv.most_similar(positive=['black', 'sun'], negative=['white']))
print('clean is to _ as pretty is to ugly:')
print(model.wv.most_similar(positive=['pretty', 'clean'], negative=['ugly']))
print('right is to _ as up is to down:')
print(model.wv.most_similar(positive=['up', 'right'], negative=['down']))
print('long is to _ as big is to small:')
print(model.wv.most_similar(positive=['big', 'long'], negative=['small']))
print('hero is to _ as good is to bad:')
print(model.wv.most_similar(positive=['good', 'hero'], negative=['bad']))
print('\n\n-------------------\n\n')
print('\n\n-------------------\n\n')


with open('w10s100', 'rb') as input:
    model = pickle.load(input)


print('model w10 s100')
print('sun is to _ as black is to white:')
print(model.wv.most_similar(positive=['black', 'sun'], negative=['white']))
print('clean is to _ as pretty is to ugly:')
print(model.wv.most_similar(positive=['pretty', 'clean'], negative=['ugly']))
print('right is to _ as up is to down:')
print(model.wv.most_similar(positive=['up', 'right'], negative=['down']))
print('long is to _ as big is to small:')
print(model.wv.most_similar(positive=['big', 'long'], negative=['small']))
print('hero is to _ as good is to bad:')
print(model.wv.most_similar(positive=['good', 'hero'], negative=['bad']))
print('\n\n-------------------\n\n')
print('\n\n-------------------\n\n')



with open('w2s1000', 'rb') as input:
    model = pickle.load(input)


print('model w2 s1000')
print('sun is to _ as black is to white:')
print(model.wv.most_similar(positive=['black', 'sun'], negative=['white']))
print('clean is to _ as pretty is to ugly:')
print(model.wv.most_similar(positive=['pretty', 'clean'], negative=['ugly']))
print('right is to _ as up is to down:')
print(model.wv.most_similar(positive=['up', 'right'], negative=['down']))
print('long is to _ as big is to small:')
print(model.wv.most_similar(positive=['big', 'long'], negative=['small']))
print('hero is to _ as good is to bad:')
print(model.wv.most_similar(positive=['good', 'hero'], negative=['bad']))
print('\n\n-------------------\n\n')
print('\n\n-------------------\n\n')



with open('w10s1000', 'rb') as input:
    model = pickle.load(input)


print('model w10 s1000')
print('sun is to _ as black is to white:')
print(model.wv.most_similar(positive=['black', 'sun'], negative=['white']))
print('clean is to _ as pretty is to ugly:')
print(model.wv.most_similar(positive=['pretty', 'clean'], negative=['ugly']))
print('right is to _ as up is to down:')
print(model.wv.most_similar(positive=['up', 'right'], negative=['down']))
print('long is to _ as big is to small:')
print(model.wv.most_similar(positive=['big', 'long'], negative=['small']))
print('hero is to _ as good is to bad:')
print(model.wv.most_similar(positive=['good', 'hero'], negative=['bad']))

