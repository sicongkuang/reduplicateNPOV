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