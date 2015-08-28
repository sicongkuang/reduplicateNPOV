__author__ = 'wxbks'
import json

f = open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/wiki_words_to_avoid.txt','r')
all_words = []
single_words = []
suffix = []
prefix = []

for line in f:
    line = line.rstrip('\n')
    nlist = line.split(',')
    for n in nlist:
        n = n.strip()
        u = n.split()
        if len(u) == 1 and '-' in n:
            nl = n.split("-")
            if nl[0] == '':
                suffix.append(nl[1])
            elif nl[1] == '':
                prefix.append(nl[0])
        else:
            all_words.append(n)

for i in all_words:
    m = i.split()
    if len(m) == 1:
        single_words.append(i)

print 'single_words',single_words

print 'all_words', all_words

print "prefix:",prefix

print "suffix:",suffix



# with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/baseline5_singlewords_list.json','w') as t2:
#     json.dump(single_words,t2)
#
#
# with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/baseline5_allWords_list.json','w') as t3:
#     json.dump(all_words,t3)
#
#
# with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/baseline5_suffix_list.json','w') as t4:
#     json.dump(suffix,t4)
#
# with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/baseline5_prefix_list.json','w') as t5:
#     json.dump(prefix,t5)


