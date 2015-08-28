__author__ = 'wxbks'
import json
feaf21_f25 = []
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/features_lst_f21f22StrongSubjectiv_context_downCase.json') as f:
    f21f22 = json.load(f)
    f.close()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/features_lst_f23f24WeakSubjectiv_context_downCase.json') as l:
    f23f24 = json.load(l)
    l.close()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/features_lst_f25_Polarity_downCase.json') as g:
    f25 = json.load(g)
    g.close()
for a,b,c in zip(f21f22,f23f24,f25):
    dic = {}
    if a['Word'] == b['Word'] == c['Word']:
        dic['Word'] = a['Word']
        dic['Strong subjective'] = a['Strong subjective']
        dic['Strong subjective in context'] = a['Strong subjective in context']
        dic['Weak subjective'] = b['Weak subjective']
        dic['Weak subjective in context'] = b['Weak subjective in context']
        dic['Polarity'] = c['Polarity']
        feaf21_f25.append(dic)
    else:
        print "problem"
        exit()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/baseline_features_lst_f21_f25.json','w') as p:
    json.dump(feaf21_f25,p)
    p.close()





tfeaf21_f25 = []
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/testdata_features_lst_f21f22StrongSubjectiv_context_downCase.json') as ft:
    tf21f22 = json.load(ft)
    ft.close()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/testdata_features_lst_f23f24WeakSubjectiv_context_downCase.json') as lt:
    tf23f24 = json.load(lt)
    lt.close()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/testdata_features_lst_f25_Polarity_downCase.json') as gt:
    tf25 = json.load(gt)
    gt.close()
for a,b,c in zip(tf21f22,tf23f24,tf25):
    dic = {}
    if a['Word'] == b['Word'] == c['Word']:
        dic['Word'] = a['Word']
        dic['Strong subjective'] = a['Strong subjective']
        dic['Strong subjective in context'] = a['Strong subjective in context']
        dic['Weak subjective'] = b['Weak subjective']
        dic['Weak subjective in context'] = b['Weak subjective in context']
        dic['Polarity'] = c['Polarity']
        tfeaf21_f25.append(dic)
    else:
        print "problem"
        exit()

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/baseline_testdata_features_lst_f21_f25.json','w') as p:
    json.dump(tfeaf21_f25,p)
    p.close()