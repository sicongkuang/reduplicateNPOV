__author__ = 'wxbks'

import xml.etree.ElementTree as ET
import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

textLst = []
indir = '/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-corpus/npov-train'
cn = 0
for fn in os.listdir(indir):
    if not fn.endswith('.xml'): continue
    fullname = os.path.join(indir, fn)
    cn += 1
    if os.path.isfile(fullname):
        tree = ET.parse(fullname)
        root = tree.getroot()
        # print root.tag
        page = root.find('{http://www.mediawiki.org/xml/export-0.7/}page')
        # print page.tag
        revision = page.findall('{http://www.mediawiki.org/xml/export-0.7/}revision')
        for s in revision:
            ## based on every revision has only one text
            t = s.find('{http://www.mediawiki.org/xml/export-0.7/}text')
            # print t.text
            textLst.append(t.text)


    else:
        print "not file"
    print str(cn) + ' / ' + str(5997)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(textLst)
word_freq_df = pd.DataFrame({'term': vectorizer.get_feature_names(), 'occurrences':np.asarray(X.sum(axis=0)).ravel().tolist()})
print word_freq_df.sort('occurrences',ascending = False).head()