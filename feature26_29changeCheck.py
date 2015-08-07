__author__ = 'wxbks'
import json

## check when down case comparison, f26-f29 change in training
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/features_lst_f26f27f28f29PositiveNegative_Context_downcaseCompare.json') as tf:
    newtrain = json.load(tf)
    tf.close()

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/features_lst_f26f27f28f29PositiveNegative_Context.json') as tf:
    oldtrain = json.load(tf)
    tf.close()

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f26f27f28f29PositiveNegative_Context_downcaseCompare.json') as tf:
    newtest = json.load(tf)
    tf.close()

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f26f27f28f29PositiveNegative_Context.json') as tf:
    oldtest = json.load(tf)
    tf.close()

for one,two in zip(newtest,oldtest):
    if one == two:
        pass
    else:
        print "old: ", two, "new: ", one
