# coding: UTF-8
from numpy import *
import operator
from os import listdir

def loadDataSet():
    postingList = [['my','dog','has','flea','problems','help','please'],
    ['maybe','not','take','him','to','dog','park','stupid'],
    ['my','dalmation','is','so','cute','I','love','him'],
    ['stop','posting','stupid','worthless','garbage'],
    ['mr','licks','ate','my','steak','how','to','stop','him'],
    ['quit','buying','worthless','dog','food','stupid']]
    
    classVec = [0.1,0,1,0,1] #1代表侮辱性文字
    return postingList, classVec
    
def createVocabList(dataSet):
    #创建一个空集
    vocabSet = set([])
    
    for document in dataSet:
        #创建两个集合的并集 ？？
        vocabSet = vocabSet | set(document)
        
    return list(vocabSet)
    
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList) #创建并初始化向量为0
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %2 is not in my Vocabulary" % word
            
    return returnVec
    

