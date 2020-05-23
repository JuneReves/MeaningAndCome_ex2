class simlexObj:
    def __init__(self, word1, word2, POS, simlex999, concW1, concW2, concQ,	assocUSF, simAssoc333, SDSimLex):
        self.word1 = word1
        self.word2 = word2
        self.POS = POS
        self.simlex999 = simlex999
        self.concW1 = concW1
        self.concW2 = concW2
        self.concQ = concQ
        self.assocUSF = assocUSF
        self.simAssoc333 = simAssoc333
        self.SDSimLex = SDSimLex

    def __str__(self):
        return self.word1 + '-' + self.word2