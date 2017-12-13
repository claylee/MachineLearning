# coding: UTF-8
from numpy import *
import operator

def createDataset():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
    
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # 计算距离
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2 
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances **0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    
    #选择距离最小的K个点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        sortedClassCount = sorted(classCount.iteritems(),
            key = operator.itemgetter(1), reverse = True)
        return sortedClassCount[0][0]
        
def file2matrix(filename):
    fr = open(filename)
    array0Lines=fr.readlines()
    numberOfLines = len(array0Lines)# 得到文本长度
    returnMat = zeros((numberOfLines,3)) #创建返回的Numpy矩阵
    classLabelVector = []
    
    index = 0 # 解析文件数据到列表
    for line in array0Lines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index +=1
        
    return returnMat, classLabelVector
    
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet= dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges,(m,1)) #特征值相除
    return normDataSet, ranges, minVals
    
def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:], \
        datingLabels[numTestVecs:m],3)
        print "this classifier came back with: %d, the real answer is : %d" \
         %(classifierResult, datingLabels[i])
        if(classifierResult != datingLabels[i]): 
            errorCount += 1.0
    print "the total error rate is : %f" %(errorCount/float(numTestVecs))
            
    
    
    
    
    
    
    
    
    
    