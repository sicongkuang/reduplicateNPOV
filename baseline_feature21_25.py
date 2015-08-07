__author__ = 'wxbks'
import json
feaf21_f25 = []
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/features_lst_f21f22StrongSubjectiv_context_downCase.json') as f:
    f21f22 = json.load(f)
    f.close()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/features_lst_f23f224WeakSubjectiv_context_downCase.json') as l:
    f23f24 = json.load(l)
    l.close()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/features_lst_f25_Polarity_downCase.json') as g:
    f25 = json.load(g)
    g.close()
for a,b,c in zip(f21f22,f23f24,f25):
    if f21f22['Word'] == f23f24['Word'] == f25['Word']:
        pass
    else:
        print "problem"
        exit()







with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/testdata_features_lst_f21f22StrongSubjectiv_context_downCase.json') as ft:
    tf21f22 = json.load(ft)
    ft.close()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/testdata_features_lst_f23f224WeakSubjectiv_context_downCase.json') as lt:
    tf23f24 = json.load(lt)
    lt.close()
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/testdata_features_lst_f25_Polarity_downCase.json') as gt:
    tf25 = json.load(gt)
    gt.close()
for a,b,c in zip(tf21f22,tf23f24,tf25):
    if tf21f22['Word'] == tf23f24['Word'] == tf25['Word']:
        pass
    else:
        print "problem"
        exit()