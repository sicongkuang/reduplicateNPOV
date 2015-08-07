__author__ = 'wxbks'
from sklearn.feature_extraction import DictVectorizer
import json
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

def logRegressionAccur():
    ## loading features from dictionaries
    vec = DictVectorizer(sparse=False)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/n_allFeatures.json') as f:
        trainX = json.load(f)
        f.close()
    for i in trainX:
        print i
        break
    trainXD = vec.fit_transform(trainX)
    for i in trainXD:
        print i
        break
    print trainXD.shape
    ## loading labels
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/single_labels_lst.json') as fl:
        trainY = json.load(fl)
        fl.close()



    print len(trainY)
    ## fit/generate logisticRegression Model
    lr = LogisticRegression()
    print "???"
    if np.any(np.isnan(trainXD)):
        print "nan in features of training"
    else:
        print "no nan in features of training"
    lr.fit(trainXD,trainY)
    print "here"
    ## loading test features
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/n_testdata_allFeatures.json') as tf:
        testX = json.load(tf)
        tf.close()
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/single_testdata_labels_lst.json') as tl:
        testYtrue = json.load(tl)
        tl.close()
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/testdata_senWlLen_lst.json') as p:
        senWlLen = json.load(p)
    b = 0
    num = 0
    denum = 0
    for i in senWlLen:
        if i == 0:
            continue
        denum += 1
        testXD = vec.transform(testX[b:b+i])
        testYXD = testYtrue[b:b+i]
        res = lr.predict_proba(testXD)
        com = []
        for t in res:
            com.append(t[1])
        m = max(com)
        maxR = [v for v,u in enumerate(com) if u==m] # assume the max is only one element
        if com[maxR[0]] > 0.5 and testYXD[maxR[0]] == 1:
            num += 1

        b = b+i
    acc = num / float(denum)
    print acc


    # testXD = vec.transform(testX)
    # print "h?"
    # testYpred = lr.predict(testXD)
    # print "come here?"
    #
    # print accuracy_score(testYtrue,testYpred)







logRegressionAccur()