__author__ = 'wxbks'
import sys

import json
reload(sys)
sys.setdefaultencoding('utf-8')
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/labels_lst.json') as fn:
        trl = json.load(fn)
        fn.close()

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/n_allFeatures.json') as fn:
        trf = json.load(fn)
        fn.close()

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/senWlLen_lst.json') as fl:
        senLen = json.load(fl)
        fl.close()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/senWl_lst_nline8.json') as t:
        senWl = json.load(t)

b=0
for inj,j in enumerate(senLen):
    print "sentence %d" % inj
    print "senWl: %s" % ', '.join(map(str,senWl[inj]))
    newtrf = trf[b:b+j]
    newtrl = trl[b:b+j]
    for i,v in enumerate(newtrf):

        print "w:%s label:%s f26:%s f27:%s f28:%s f29:%s" % (v['Word'],newtrl[i],v['Positive word'],v['Positive word in context'],v['Negative word'],v['Negative word in context'])

    if inj == 10:
        break
    b = b+j
fl.close()