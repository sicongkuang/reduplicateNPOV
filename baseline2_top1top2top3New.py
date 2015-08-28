__author__ = 'wxbks'



import json
import operator

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/features_lst_f30_V341_stanfordTypedD.json') as t:
    f30 = json.load(t)

role_freq = dict()
num_words = len(f30)

for i in f30:
    gr =  i['Grammatical relation']
    if gr in role_freq:
        role_freq[gr] += 1
    else:
        role_freq[gr] = 1


role_ratio = dict()

for a in role_freq:
    role_ratio[a] = role_freq[a]/float(num_words)

sorted_roleFreq = sorted(role_freq.items(), key=operator.itemgetter(1),reverse=True)
sorted_roleRatio = sorted(role_ratio.items(), key=operator.itemgetter(1),reverse=True)

print "sorted_roleFreq"
print sorted_roleFreq
print "sorted_roleRatio"
print sorted_roleRatio

## top1
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f30_V341_stanfordTypedD.json') as t:
    f30 = json.load(t)

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/single_testdata_labels_lst.json') as l:
    testlab = json.load(l)

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_senWlLen_lst.json') as s:
    testLen = json.load(s)

b = 0
sum1 = 0
sum2 = 0
sum3 = 0
denom = 0
for i in testLen:

    if i == 0:
        continue
    denom += 1
    tmp = f30[b:b+i]
    lab = testlab[b:b+i]
    top3Lst = []
    for r in sorted_roleRatio:
        if len(top3Lst) == 3:
                break
        for ind,val in enumerate(tmp):
            if len(top3Lst) == 3:
                break

            if r[0] == val['Grammatical relation'] and len(top3Lst) < 3:
                top3Lst.append((ind,val['Grammatical relation']))

    print "top3Lst"
    print top3Lst

    # top1
    top1_lab = top3Lst[0][0]
    if lab[top1_lab] == 1:
        sum1 += 1
    top2_lab = top3Lst[1][0]
    if lab[top1_lab] == 1 or lab[top2_lab] == 1:
        sum2 += 1
    top3_lab = top3Lst[2][0]
    if lab[top1_lab] == 1 or lab[top2_lab] == 1 or lab[top3_lab] == 1:
        sum3 += 1
    b = b + i

print "sum1:"
print sum1
print "sum2:"
print sum2
print "sum3:"
print sum3
print "denom:"
print denom
print "top1:"
print sum1/float(denom)
print "top2:"
print sum2/float(denom)
print "top3:"
print sum3/float(denom)


biasedProb = [(u'possessive', 0.5), (u'root', 0.14402907580477675), (u'acomp', 0.13709677419354838), (u'csubj', 0.10526315789473684), (u'number', 0.10416666666666667), (u'prt', 0.09951060358890701), (u'iobj', 0.09714285714285714), (u'dep', 0.09617668012348611), (u'amod', 0.09503097403453276), (u'advmod', 0.09118612283169245), (u'pobj', 0.08999309074159373), (u'nsubj', 0.08737137511693172), (u'rcmod', 0.08680339755541744), (u'xcomp', 0.08600064662140317), (u'nn', 0.08129474434227937), (u'conj', 0.07965421426366162), (u'nsubjpass', 0.079155672823219), (u'advcl', 0.07868852459016394), (u'pcomp', 0.07493540051679587), (u'dobj', 0.07467348097671778), (u'tmod', 0.07392996108949416), (u'vmod', 0.07359781121751026), (u'npadvmod', 0.07051282051282051), (u'num', 0.06735306735306736), (u'ccomp', 0.06326797385620915), (u'auxpass', 0.061025223759153785), (u'cop', 0.06028833551769332), (u'expl', 0.057692307692307696), (u'poss', 0.057645134914145545), (u'predet', 0.056818181818181816), (u'aux', 0.056149330121932864), (u'neg', 0.05268199233716475), (u'mark', 0.049096921902823706), (u'mwe', 0.04817275747508306), (u'quantmod', 0.0425531914893617), (u'det', 0.041296296296296296), (u'cc', 0.03848454636091725), (u'prep', 0.03736133791317078), (u'preconj', 0.023255813953488372)]

b = 0
sum1 = 0
sum2 = 0
sum3 = 0
denom = 0
for i in testLen:

    if i == 0:
        continue
    denom += 1
    tmp = f30[b:b+i]
    lab = testlab[b:b+i]
    top3Lst = []
    for r in biasedProb:
        if len(top3Lst) == 3:
                break
        for ind,val in enumerate(tmp):
            if len(top3Lst) == 3:
                break

            if r[0] == val['Grammatical relation'] and len(top3Lst) < 3:
                top3Lst.append((ind,val['Grammatical relation']))

    print "top3Lst"
    print top3Lst

    # top1
    top1_lab = top3Lst[0][0]
    if lab[top1_lab] == 1:
        sum1 += 1
    top2_lab = top3Lst[1][0]
    if lab[top1_lab] == 1 or lab[top2_lab] == 1:
        sum2 += 1
    top3_lab = top3Lst[2][0]
    if lab[top1_lab] == 1 or lab[top2_lab] == 1 or lab[top3_lab] == 1:
        sum3 += 1
    b = b + i

print "sum1:"
print sum1
print "sum2:"
print sum2
print "sum3:"
print sum3
print "denom:"
print denom
print "top1:"
print sum1/float(denom)
print "top2:"
print sum2/float(denom)
print "top3:"
print sum3/float(denom)