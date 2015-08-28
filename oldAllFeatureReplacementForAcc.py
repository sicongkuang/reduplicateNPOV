__author__ = 'wxbks'
import json

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/n_testdata_allFeatures_fixdedF31F26_F29F21_F25F19F20F17F18F15F16F13F14F11F12.json') as f:
    old_allfea_f31f26_f29F21_F25F19F20F17F18F15F16F13F14F11F12 = json.load(f)

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f9f10hedge_hedgeInContext_downCase.json') as fb:
    fixedf9f10 = json.load(fb)
# modNo =0
for one,two in zip(old_allfea_f31f26_f29F21_F25F19F20F17F18F15F16F13F14F11F12,fixedf9f10):

    if one['Word'] == two['Word']:
        one['Hedge'] = two['Hedge']
        one['Hedge in context'] = two['Hedge in context']

    else:
        print "word: %s is not match" % one['word']
        exit()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/n_testdata_allFeatures_fixdedF31F26_F29F21_F25F19F20F17F18F15F16F13F14F11F12F9F10.json','w') as t:
    json.dump(old_allfea_f31f26_f29F21_F25F19F20F17F18F15F16F13F14F11F12,t)
# print "modify feature 31 times: %d" % modNo


