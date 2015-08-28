__author__ = 'wxbks'
import json
import numpy as np
from sklearn.feature_extraction import DictVectorizer

# with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_labels_lst.json') as fl:
#         trainY = json.load(fl)
#         fl.close()
# for g,q in enumerate(trainY):
#     trainY[g] = trainY[g][1]
# with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/single_testdata_labels_lst.json','w') as t:
#     json.dump(trainY,t)
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/allFeaturesDownCaseV2.json') as f:
        trainX = json.load(f)
        f.close()
# vec = DictVectorizer()
# trainXD = vec.fit_transform(trainX).toarray()
# if np.any(np.isnan(trainXD)):
#     print "nan in features of training"
# g=0
# for i,j in zip(trainY,trainX):
#     if i[0] == j['Word']:
#         pass
#         g+=1
#         print "processing word %d" % g
#     else:
#         print "not match"
#         exit()
g=0
for d in trainX:
    for key in d.iterkeys():
        if key != 'Word' and key != 'Lemma' and d[key] == None:
            d[key] = 'NA'
            g += 1
            print "modify None %d" % g
print "done with training ..."

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/n_allFeaturesDownCaseV2.json','w') as fn:
        json.dump(trainX,fn)
        fn.close()

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_allFeaturesDownCaseV2.json') as ft:
        testX = json.load(ft)
        ft.close()

g=0
for d in testX:
    for key in d.iterkeys():
        if key != 'Word' and key != 'Lemma' and d[key] == None:
            d[key] = 'NA'
            g += 1
            print "modify None %d" % g
print "done with testing ..."

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/n_testdata_allFeaturesDownCaseV2.json','w') as fte:
        json.dump(testX,fte)