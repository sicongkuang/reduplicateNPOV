__author__ = 'wxbks'

import json

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f30_V341_stanfordTypedD.json') as f:
    testAllfea = json.load(f)
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/single_testdata_labels_lst.json') as l:
    testlab = json.load(l)
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_senWlLen_lst.json') as s:
    testLen = json.load(s)
denum = 0
num = 0
b = 0
for i in testLen:
    if i == 0:
        continue
    denum += 1
    sen = testAllfea[b:b+i]
    lab = testlab[b:b+i]
    for one,two in zip(sen,lab):
        # if (one['Grammatical relation'] == 'nmod' and two == 1) or (one['Grammatical relation'] == 'compound' and two == 1) or (one['Grammatical relation'] == 'amod' and two == 1):
        if (one['Grammatical relation'] == 'root' and two == 1) or (one['Grammatical relation'] == 'poss' and two == 1) or (one['Grammatical relation'] == 'csubj' and two == 1):
            num += 1
    b = b+i

print "num:%d , denum:%d" % (num,denum)
acc = num/float(denum)

print "top1:", acc