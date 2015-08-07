__author__ = 'wxbks'
from nltk.stem import WordNetLemmatizer
import json

wordnet_lemmatizer = WordNetLemmatizer()

with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/npov_words.txt') as f:
    biasLex  = json.load(f)
    f.close()
print "without lemma, ",len(biasLex.keys())

for key in biasLex.keys():
    newKey = key.lower()
    w = biasLex.pop(key)
    if newKey not in biasLex:
        biasLex[newKey] = w
    else:
        biasLex[newKey] = w + biasLex[newKey]
print " downcase: ", len(biasLex.keys())
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/npov_words_downCase.json','w') as t:
    json.dump(biasLex,t)

for key in biasLex.keys():
    newKey = wordnet_lemmatizer.lemmatize(key)
    w = biasLex.pop(key)
    if newKey not in biasLex:
        biasLex[newKey] = w
    else:
        biasLex[newKey] = w + biasLex[newKey]
print "after lemma and downcase: ", len(biasLex.keys())
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/npov_words_lemma_downcase.json','w') as l:
    json.dump(biasLex,l)

for k,v in biasLex.items():
    if v<2:
        print "del: %s %d" % (k,v)
        del biasLex[k]
print "downcase, lemma and at least 2 times: ", len(biasLex.keys())
with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/npov_words_lemma_2_downcase.json','w') as g:
    json.dump(biasLex,g)
