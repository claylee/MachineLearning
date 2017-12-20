# coding: UTF-8
from numpy import *
import operator

def loadDataSet():
    dataMat = [];
    labelMat = [];

    Dict6 = []
    Dict9 = []

    fr = open('testSet.txt');
    for line in fr.readlines():
        lineArr = line.strip().split(',')
        #print lineArr[6]
        dataMat.append([1.0, float(lineArr[6]), float(lineArr[8])])
        labelMat.append(int(lineArr[0]))
        if lineArr[6] not in Dict6:
            Dict6.append(lineArr[6])

        if lineArr[9] not in Dict9:
            Dict9.append(lineArr[9])

    return dataMat, labelMat, Dict6 ,Dict9

def createVocabList(dataSet):
    vecSet = set([])

def setList2Vec(vocabList, inputSet, idx):
    returnVec = [0]*len(vocabList) #创建并初始化向量为0
    print vocabList
    print arrayE
    for arrayE in inputSet:
        print arrayE[idx]
        word = arrayE[idx]
        print word
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %f is not in my Vocabulary" % word

        arrayE = returnVec

dataMat, labelMat, Dict6, Dict9 = loadDataSet()
print dataMat
setList2Vec(Dict6,dataMat,1)
print dataMat
