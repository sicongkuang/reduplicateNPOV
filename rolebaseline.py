__author__ = 'wxbks'
import json
import operator

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/features_lst_f30_V341_stanfordTypedD.json') as f:
    allFea = json.load(f)
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/single_labels_lst.json') as l:
    labels = json.load(l)

#
# with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f30_V341_stanfordTypedD.json') as f:
#     allFea = json.load(f)
# with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/single_testdata_labels_lst.json') as l:
#     labels = json.load(l)

roleBaseline = {}
syntacFreq = {}
for one,lab in zip(allFea,labels):
    gr = one['Grammatical relation']
    if gr in syntacFreq:
        syntacFreq[gr] += 1
    else:
        syntacFreq[gr] = 1


    if lab == 1:

        if gr in roleBaseline:
            roleBaseline[gr] += 1
        else:
            roleBaseline[gr] = 1



# print roleBaseline

sorted_roleBaseline = sorted(roleBaseline.items(), key=operator.itemgetter(1),reverse=True)
print "bias freq:",sorted_roleBaseline

ratioBase = dict()

# sum = 0
# for i,v in roleBaseline.iteritems():
#     sum += v
# print "sum:",sum
for key in roleBaseline:
    ratioBase[key] = roleBaseline[key]/float(syntacFreq[key])
ratio2 = dict(ratioBase)
for ev in ratio2.keys():
    if syntacFreq[ev] <= 500:

        ratio2.pop(ev)


# print ratioBase
sorted_ratioBase = sorted(ratioBase.items(), key=operator.itemgetter(1), reverse=True)
print "bias prob",sorted_ratioBase
sorted_syntacFreq = sorted(syntacFreq.items(), key=operator.itemgetter(1), reverse=True)
print "number of gr:",len(sorted_ratioBase)
print "all gr:",sorted_syntacFreq

sorted_ratio2 = sorted(ratio2.items(), key=operator.itemgetter(1), reverse=True)
print "<500 del:    ",sorted_ratio2





