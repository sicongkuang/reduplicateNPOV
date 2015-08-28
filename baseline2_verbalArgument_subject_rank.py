__author__ = 'wxbks'

import json
import operator

# verbal_argument = ['acomp','advcl','agent','auxpass','ccomp','cop','dobj','iobj','xcomp','vmod']
# verbal_argument = ['acomp','advcl','agent','aux','auxpass','ccomp','cop','dobj','expl','iobj','parataxis','xcomp','vmod']

# subject = ['csubj','csubjpass','nsubj','nsubjpass','xsubj']
subject = ['csubj','amod']

verbal_argument = ['acomp','iobj','prt','number','dep','dobj']


with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/features_lst_f30_V341_stanfordTypedD.json') as f:
    f30_stan = json.load(f)
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/single_labels_lst.json') as l:
    labels = json.load(l)

corpRoleCount = {'verbal argument':0,'subject':0}

roleBaisedCount = {'verbal argument':0,'subject':0}

for one,lab in zip(f30_stan,labels):
    gr = one['Grammatical relation']
    if gr in verbal_argument:
        corpRoleCount['verbal argument'] += 1
    elif gr in subject:
        corpRoleCount['subject'] += 1
    else:

        if gr in corpRoleCount:
            corpRoleCount[gr] += 1
        else:
            corpRoleCount[gr] = 1


    if lab == 1:
        if gr in verbal_argument:
            roleBaisedCount['verbal argument'] += 1
        elif gr in subject:
            roleBaisedCount['subject'] += 1
        else:
            if gr in roleBaisedCount:
                roleBaisedCount[gr] += 1
            else:
                roleBaisedCount[gr] = 1

sorted_roleBaisedCount = sorted(roleBaisedCount.items(), key=operator.itemgetter(1),reverse=True)
sorted_corpRoleCount = sorted(corpRoleCount.items(), key=operator.itemgetter(1),reverse=True)

ratioRoleBaisedProb = {}

for key in roleBaisedCount:
    ratioRoleBaisedProb[key] = roleBaisedCount[key]/float(corpRoleCount[key])

sorted_ratioRoleBaisedProb = sorted(ratioRoleBaisedProb.items(), key=operator.itemgetter(1),reverse=True)

# result
print "sorted copors role Count:"
print sorted_corpRoleCount

print "sorted roleBaisedCount:"
print sorted_roleBaisedCount

print "sorted ratioRoleBaisedCount:"
print sorted_ratioRoleBaisedProb

for i,v in enumerate(sorted_ratioRoleBaisedProb):
    if v[0]=='verbal argument':
        print 'verbal argument',i+1,v
    elif v[0]=='subject':
        print 'subject',i+1,v


#accuracy
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f30_V341_stanfordTypedD.json') as f:
    testAllfea = json.load(f)
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/single_testdata_labels_lst.json') as l:
    testlab = json.load(l)
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_senWlLen_lst.json') as s:
    testLen = json.load(s)
denum = 0
num = 0
b = 0

# for i in testAllfea:
#     gr = i['Grammatical relation']
#     if gr in verbal_argument:
#         i['Grammatical relation'] = 'verbal argument'
#     elif gr in subject:
#         i['Grammatical relation'] = 'subject'
#     else:
#
#         pass

for i in testLen:
    if i == 0:
        continue
    denum += 1
    sen = testAllfea[b:b+i]
    lab = testlab[b:b+i]
    for one,two in zip(sen,lab):
        # if (one['Grammatical relation'] == 'nmod' and two == 1) or (one['Grammatical relation'] == 'compound' and two == 1) or (one['Grammatical relation'] == 'amod' and two == 1):
        if (one['Grammatical relation'] == 'prep' and two == 1) or (one['Grammatical relation'] == 'pobj' and two == 1):# or (one['Grammatical relation'] == 'nn' and two == 1):
            num += 1
    b = b+i

print "num:%d , denum:%d" % (num,denum)
acc = num/float(denum)

print "top1:", acc