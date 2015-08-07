#-*- coding: utf-8 -*-
# from __future__ import print_function
__author__ = 'wxbks'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xml.etree.ElementTree as ET
import os
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import json
import codecs
import unicodedata
def getFreqArt(w):
    # input: a word
    # output: how many of this word appears in this artName
    # assume: frequency of all words in article has been calculated
    try:
        a = d[w]
    except KeyError, e:
        print 'I got a Key Error - the word could not found in article is: %s' % w
        return -1
    return a

def getCount(artName):
    # process article
    artLst = []
    artDict = {}
    for fn in os.listdir(indir):
        if not fn.endswith('.xml'): continue
        print fn
        if ':' in fn:
            fn = fn.replace(':','/')
        fn = fn.decode('utf-8')
        fn = unicodedata.normalize("NFC",fn)
        newfn = fn[:-4]


        if newfn == artName:
            print "found article begin processing"
            if '/' in fn:
                fn = fn.replace('/',':')
            fullname = os.path.join(indir, fn)
            tree = ET.parse(fullname)
            root = tree.getroot()
            page = root.find('{http://www.mediawiki.org/xml/export-0.7/}page')

            revisions = page.findall('{http://www.mediawiki.org/xml/export-0.7/}revision')
            for s in revisions:
                txt = s.find('{http://www.mediawiki.org/xml/export-0.7/}text')
                artLst.append(txt.text)
            artLst = filter(None,[one for one in artLst])
            print "processing done; begin counting"
            vectorizer = CountVectorizer(min_df=1,token_pattern='([^\[\|\]\s\.\!\=\{\}\;\<\>\?\"\'\#\(\)\,\*]+)',lowercase=False)
            X = vectorizer.fit_transform(artLst)
            artDict = dict(zip(vectorizer.get_feature_names(),np.asarray(X.sum(axis=0)).ravel()))
            print vectorizer.get_feature_names()
            return artDict



        # fullname = os.path.join(indir, fn)
        #
        # if os.path.isfile(fullname):
        #     tree = ET.parse(fullname)
        #     root = tree.getroot()
        #     # print root.tag
        #     page = root.find('{http://www.mediawiki.org/xml/export-0.7/}page')
        #     # print page.tag
        #     title = page.find('{http://www.mediawiki.org/xml/export-0.7/}title')
        #
        #     if title.text == artName:
        #         # found article
        #         print fn
        #         # article to list
        #
        #         revisions = page.findall('{http://www.mediawiki.org/xml/export-0.7/}revision')
        #         # print page[3]
        #         for s in revisions:
        #             id = s.find('{http://www.mediawiki.org/xml/export-0.7/}id')
        #             print id.text
        #             txt = s.find('{http://www.mediawiki.org/xml/export-0.7/}text')
        #             # print txt.text
        #             artLst.append(txt.text)
        #         print len(artLst)
        #         vectorizer = CountVectorizer(min_df=1,token_pattern='([^\[\|\]\s\.\!\=\{\}\;\<\>\?\"\'\#\(\)\,]+)',lowercase=False)
        #         # # print artLst
        #         # with open('/Users/wxbks/Downloads/artLst.txt','w') as f:
        #         #     json.dump(artLst,f)
        #         print "here"
        #         # f = codecs.open('/Users/wxbks/Downloads/artLst.txt','w','utf-8')
        #         # for one in artLst:
        #         #     # one = one.decode('utf-8')
        #         #     if one == None:
        #         #         print "this is NOne!!!!!!!!"
        #         #         artLst.remove(one)
        #         #
        #         #     f.write(one.encode('utf-8')+'\n==================\n==================\n================\n')
        #         # print "over"
        #         # f.close()
        #         artLst = filter(None,[one for one in artLst])
        #         X = vectorizer.fit_transform(artLst)
        #         # word_freq_df = pd.DataFrame({'term': vectorizer.get_feature_names(), 'occurrences':np.asarray(X.sum(axis=0)).ravel().tolist()})
        #         # word_freq_df['frequency'] = word_freq_df['occurrences']/np.sum(word_freq_df['occurrences'])
        #         # print word_freq_df.sort('occurrences',ascending = False).head()
        #         print vectorizer.get_feature_names()
        #         artDict = dict(zip(vectorizer.get_feature_names(),np.asarray(X.sum(axis=0)).ravel()))
        #         return artDict


                # print word_freq_df['occurences']['outdueled']
                # sklearn.feature_extraction.text.CountVectorizer(vocabulary=['outdueled','peacock'])

                # return artLst



            # for s in revision:
            #     ## based on every revision has only one text
            #     t = s.find('{http://www.mediawiki.org/xml/export-0.7/}id')
            #     print t.text
            #     if t.text == id:
            #         print "found!"
            #         return fn





indir = '/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-corpus_bak/testArticleName'
# cn = 0
# for fn in os.listdir(indir):
#     if not fn.endswith('.xml'): continue
#     fullname = os.path.join(indir, fn)
#     cn += 1
#     if os.path.isfile(fullname):
#         tree = ET.parse(fullname)
#         root = tree.getroot()
#         # print root.tag
#         page = root.find('{http://www.mediawiki.org/xml/export-0.7/}page')
#         # print page.tag
#         revision = page.findall('{http://www.mediawiki.org/xml/export-0.7/}revision')
#         for s in revision:
#             ## based on every revision has only one text
#             t = s.find('{http://www.mediawiki.org/xml/export-0.7/}text')
#             # print t.text
#             # textLst.append(t.text)
d = {}
editWordNotFoundArticle = []
d = getCount(u'Alarm für Cobra 11/ Highway Nights')
print getFreqArt(u'the')

