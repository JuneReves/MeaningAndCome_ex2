#This should only be used once to build a simlex object

import pickle
from simlexobj import simlexObj
        
objList = list()

with open('SimLex-999/SimLex-999.txt') as f:
    firstline = True
    for line in f.readlines():
        if firstline:
            firstline = False
            continue;
        line = line.replace('\n', '')
        line = line.split('\t')
        objList.append(simlexObj(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9]))

with open('simlexObj', 'wb') as output:
    pickle.dump(objList, output, pickle.HIGHEST_PROTOCOL)