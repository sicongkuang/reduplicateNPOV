__author__ = 'wxbks'
import json

def genAllFeaturesFile():
    '''
    input all the feature file
    :return: a file with all the features
    '''
    # allf = open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_POSITIONinSentence.json') as f8file:
        f8 = json.load(f8file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_word_lemma_pos_pos1_pos2.json') as f2tof7file:
        f2tof7 = json.load(f2tof7file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f9f10hedge_hedgeInContext.json') as f9f10file:
        f9f10 = json.load(f9f10file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f11f12Factive.json') as f11f12file:
        f11f12 = json.load(f11f12file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f13f14Assertive.json') as f13f14file:
        f13f14 = json.load(f13f14file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f15f16Implicative.json') as f15f16file:
        f15f16 = json.load(f15f16file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f17f18Report.json') as f17f18file:
        f17f18 = json.load(f17f18file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f19f20Entailment.json') as f19f20file:
        f19f20 = json.load(f19f20file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f21f22StrongSubjectiv_context.json') as f21f22file:
        f21f22 = json.load(f21f22file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f23f24WeakSubjectiv_context.json') as f23f24f25file:
        f23tof25 = json.load(f23f24f25file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f26f27f28f29PositiveNegative_Context.json') as f26tof29file:
        f26tof29 = json.load(f26tof29file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f30GrammaticalRelation.json') as f30file:
        f30 = json.load(f30file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f31BiasLex.json') as f31file:
        f31 = json.load(f31file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f32CollaborativeFea.json') as f32file:
        f32 = json.load(f32file)
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/testdata_features_lst_f25Polarity.json') as f25file:
        f25 = json.load(f25file)

    allFea = []
    o = 0
    for a, b,c,d,e,f,g,h,i,j,k,l,m,n,p in zip(f2tof7,f8,f9f10,f11f12,f13f14,f15f16,f17f18,f19f20,f21f22,f23tof25,f26tof29,f30,f31,f32,f25):
        o+=1
        z = dict()
        if a["Word"]==b["Word"]==c["Word"]==d["Word"]==e["Word"]==f["Word"]==g["Word"]==h["Word"]==i["Word"]==j["Word"]==k["Word"]==l["Word"]==m["Word"]==n["Word"]:
            z["Word"] = a["Word"]
            z["Lemma"] = a["Lemma"]
            z["POS"] = a["POS"]
            z["POS-1"] = a["POS-1"]
            z["POS+1"] = a["POS+1"]
            z["POS-2"] = a["POS-2"]
            z["POS+2"] = a["POS+2"]
            z["Position in sentence"] = b["Position in sentence"]
            z['Hedge'] = c["Hedge"]
            z['Hedge in context'] = c["Hedge in context"]
            z["Factive verb"] = d["Factive verb"]
            z["Factive verb in context"] = d["Factive verb in context"]
            z["Assertive verb"] = e["Assertive verb"]
            z["Implicative verb"] = f["Implicative verb"]
            z["Implicative verb in context"] = f["Implicative verb in context"]
            z["Report verb"] = g["Report verb"]
            z["Report verb in context"] = g["Report verb in context"]
            z["Entailment"] = h["Entailment"]
            z["Entailment in context"] = h["Entailment in context"]
            z["Strong subjective"] = i["Strong subjective"]
            z["Strong subjective in context"] = i["Strong subjective in context"]
            z["Weak subjective"] = j["Weak subjective"]
            z["Weak subjective in context"] = j["Weak subjective in context"]
            z["Polarity"] = p["Polarity"]
            z["Positive word"] = k["Positive word"]
            z["Positive word in context"] = k["Positive word in context"]
            z["Negative word"] = k["Negative word"]
            z["Negative word in context"] =k["Negative word in context"]
            z["Grammatical relation"] = l["Grammatical relation"]
            z["Bias lexicon"] = m["Bias lexicon"]
            z["Collaborative feature"] = n["Collaborative feature"]


        else:
            print "problem of the number of word:%s" % a["Word"]
            exit()
        allFea.append(z)
        print "processing %d of 267980" % o
    with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/testdata_allFeatures.json','w') as fp:
        json.dump(allFea,fp)
    # json.load('/Volumes/Seagate Backup Plus Drive/npov_paper_data/infoFile1/features_lst_word_lemma_pos_pos1_pos2.json')


genAllFeaturesFile()