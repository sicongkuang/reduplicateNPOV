__author__ = 'wxbks'
import json
import pandas as pd
import numpy as np

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/baseline5_singlewords_list.json') as f:
    singleWordList = json.load(f)


with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/baseline5_suffix_list.json') as t4:
    suffix = json.load(t4)

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/baseline5_prefix_list.json') as t5:
    prefix = json.load(t5)

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f30_V341_stanfordTypedD.json') as t:
    corpus_words = json.load(t)

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/single_testdata_labels_lst.json') as l:
    testlab = json.load(l)

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_senWlLen_lst.json') as s:
    testLen = json.load(s)


## top 1
b = 0
g = 0 ## cumulative of top1 of each sentence
g2 = 0 ## cumulative of top2 of each sentence
g3 = 0 ## cumulative of top3 of each sentence
senNum = 0
top1Lst = [] ## top1 lst
top2Lst = []
top3Lst = []
for i in testLen:
    if i == 0:
        continue
    senNum += 1
    lab = testlab[b:b+i] # true label
    words = corpus_words[b:b+i]
    wlst = []
    for w in words:
        wlst.append(w['Word'])
    # count biased words as appearing in singleWordList
    appearinS = []
    for wo in wlst:
        if '-' not in wo and wo.lower() in singleWordList:
            appearinS.append((wo,1))
        elif '-' not in wo and wo.lower() not in singleWordList:
            appearinS.append((wo,0))
        elif '-' in wo:
            ls = wo.split('-')
            if ls[0] and ls[0].lower() in prefix:
                appearinS.append((wo,1))
            elif ls[1] and ls[1].lower() in suffix:
                appearinS.append((wo,1))
            else:
                appearinS.append((wo,0))

    print appearinS
    # top1
    denom = 0
    num = 0
    numN = 0
    top1 = 0
    for ins,a in enumerate(appearinS):
        denom += a[1]
        if a[1] == 1 and lab[ins] == 1:
            num += 1
        elif a[1] == 1 and lab[ins] == 0:
            numN += 1
    if denom == 0 or num == 0:
         top1 = 0
    else:
        top1 = num/float(denom)
    g += top1

    top1Lst.append(top1)
    print "top1",top1
    # denom might be 0

    # top2
    if denom == 0:
        top2 = 0
    else:
        if numN == 0:
            top2 = 1 # top1 should be 1 also
        else:
            if denom - 1 == 0:
                top2 = 0
            elif numN - 1 == 0:
                top2 = 1
            else:
                n_t1 = (numN/float(denom))
                n_t2 = (numN - 1)/float((denom-1))
                top2 = 1 - n_t1*n_t2

    g2 += top2
    top2Lst.append(top2)


    #top3
    if denom == 0:
        top3 = 0
    else:
        if numN == 0:
            top3 = 1
        else:
            if denom - 1 == 0:
                top3 = 0
            elif numN - 1 == 0:
                top3 = 1
            else:
                if denom - 2 == 0:
                    top3 = 0
                elif numN - 2 == 0:
                    top3 = 1
                else:
                    n_t1 = (numN/float(denom))
                    n_t2 = (numN - 1)/float((denom-1))
                    n_t3 = (numN - 2)/float((denom-2))
                    top3 = 1 - n_t1*n_t2*n_t3

    g3 += top3
    top3Lst.append(top3)


    b= b + i

s = pd.Series(np.array(top1Lst))
print s.describe()
print "top1:"
print g/float(senNum)
print "top2:"
print g2/float(senNum)
print "top3:"
print g3/float(senNum)
s = pd.Series(np.array(top2Lst))
print s.describe()
s = pd.Series(np.array(top3Lst))
print s.describe()