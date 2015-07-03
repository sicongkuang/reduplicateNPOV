# -*- coding: utf-8 -*-
# from __future__ import print_function
__author__ = 'wxbks'
import re
import string

from nltk.metrics import *
from HTMLParser import HTMLParser
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords
import os
from nltk.parse import stanford
import StanfordDependencies
import timeit
import codecs


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def strip_http(str):
    str = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', str)
    # re.sub(r'^https?:\/\/.*[\r\n]*', '', str)
    return str

# def editsWordsList(str):
#     '''
#         return list of words in the string
#     '''
#     wordl = []
#     wordl = re.compile('\w+').findall(str.strip('.,/"=:<>').lower())
#     return wordl

def editsWordsList(str):
    '''
        return list of words in the string
        e.g: str = "-this is. A - sentence;one-word what's"
        """ Output:
        ['this', 'is', 'A', 'sentence', 'one-word', "what's"]
        """
    '''
    wordl = []
    # wordl = re.compile('\w+').findall(str.strip('.,/"=:<>').lower())
    wordl = filter(None,[word.strip(string.punctuation)
                 for word in str.replace(';','; ').split()
                 ])
    # print wordl
    return wordl

def editsLess(num):
    if num <= 5:
        return True
    else:
        return False

def checkHttpLink(lst):
    '''
    return false if the list only contain urls
    :param str2: input the list of the difference
    '''
    # urls = []
    if lst == [] or lst == ['']:
        return False # if two string equal or post is empty(delete), tuple is good
    for s in lst:
        if len(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', s)) != 0:
            lst.remove(s)
    if len(lst) == 0:
        return True # bad tuple,delete it
    else:
        return False # good tuple

# in use
def checkHttpOnly(str0,str1):
    f0 = filter(None,re.split('[\[\]\s]',str0))
    f1 = filter(None,re.split('[\[\]\s]',str1))
    nl = list(set(f1).symmetric_difference(set(f0)))
    # filter all punctuations
    unpuncL = [i for i in nl if any(j not in string.punctuation and not j.isdigit() for j in i)]
    return checkHttpLink(unpuncL) # filter out the tuple which only differ by url

def stripped(test_str):
    ret = ''
    skip1c = 0 #[
    skip2c = 0 #<
    skip3c = 0 #{
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '<':
            skip2c += 1
        elif i == '{':
            skip3c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ']' and skip1c == 0:
            continue
        elif i == '>'and skip2c > 0:
            skip2c -= 1
        elif i == '>' and skip2c == 0:
            continue
        elif i == '}' and skip3c > 0:
            skip3c -= 1
        elif i == '}' and skip3c == 0:
            continue
        elif skip1c == 0 and skip2c == 0 and skip3c == 0:
            ret += i
    return ret

def strippedNoSquBrac(test_str):
    ret = ''
    # skip1c = 0 #[
    skip2c = 0 #<
    skip3c = 0 #{
    for i in test_str:
        if i == '<':
            skip2c += 1
        elif i == '{':
            skip3c += 1
        elif i == '>'and skip2c > 0:
            skip2c -= 1
        elif i == '>' and skip2c == 0:
            continue
        elif i == '}' and skip3c > 0:
            skip3c -= 1
        elif i == '}' and skip3c == 0:
            continue
        elif skip2c == 0 and skip3c == 0:
            ret += i
    return ret

def check5gram(str):
    if len(editsWordsList(stripped(str))) <= 5:
        return False
    else:
        return True


def brackets0digit(str):
    str = strippedNoSquBrac(str)

    wordl = filter(None,[word.strip(string.punctuation)
                 for word in str.replace(';','; ').split() if not word.isdigit()
                 ])
    if len(wordl) == 0:

        return True
    else:

        return False

# def extractSenWord2list():

def stripBrackDigitPun(str):
    # dict = {}
    str1 = stripped(str)
    wordl = filter(None,[word.strip(string.punctuation)
                 for word in str.replace(';','; ').split() if not word.isdigit()
                 ])
    return wordl

# # def extractSenWord2list(str):
# def checkSquarBrac(str1,str2):
#     if '[' in str1 and '[' in str2:
#         nos1 = stripped(str1)
#         nos2 = stripped(str2)
#         wordl1 = filter(None,[word.strip(string.punctuation)
#                  for word in nos1.split() if not word.isdigit()
#                  ])
#         wordl2 = filter(None,[word.strip(string.punctuation)
#                  for word in nos1.split() if not word.isdigit()
#                  ])
#         if set(wordl1) == set(wordl2):
#
#         else: return False
#     elif '[' not in str1 or '[' not in str2:
#         return False

def checkSquarBrac(str1,str2):
    if '[' in str1 and '[' in str2:
        nos1 = stripped(str1)
        nos2 = stripped(str2)
        wordl1 = filter(None,[word.strip(string.punctuation)
                 for word in nos1.split() if not word.isdigit()
                 ])
        wordl2 = filter(None,[word.strip(string.punctuation)
                 for word in nos2.split() if not word.isdigit()
                 ])
        str1 = strippedNoSquBrac(str1)
        str2 = strippedNoSquBrac(str2)
        if set(wordl1) == set(wordl2):
            if '[' in str1 and ']' in str1:
                slist1 = re.findall('\[.*?\]',str1)
            else:
                slist1 = re.findall('\[.*',str1)
            if '[' in str1 and ']' in str2:
                slist2 = re.findall('\[.*?\]',str2)
            else:
                slist2 = re.findall('\[.*',str2)

            slist1_ = filter(None,[word.strip(string.punctuation)
                 for word in slist1 if not word.isdigit()
                 ])
            slist2_ = filter(None,[word.strip(string.punctuation)
                 for word in slist2 if not word.isdigit()
                 ])
            for ins1, sl1 in enumerate(slist1_):
                if '|' in sl1:
                    res1 = sl1.split('|')
                    slist1_[ins1] = res1[-1]
            for ins2, sl2 in enumerate(slist2_):
                if '|' in sl2:
                    res2 = sl2.split('|')
                    slist2_[ins2] = res2[-1]

            if len(slist1_) != len(slist2_):
                return False
            elif set(slist1_) == set(slist2_):
                return True
            else:
                return False

        else: return False
    elif '[' not in str1 or '[' not in str2:
        return False

def squrBracParse(str):
    if '[' in str and ']' in str:
        slist = re.findall('\[.*?\]',str)


    elif '[' in str and ']' not in str:
        slist = re.findall('\[.*',str)
    else:
        return str

    for ins, sl in enumerate(slist):
        if '|' in sl:

            res1 = sl.split('|')

            str = str.replace(sl,' '+res1[-1])

    return str


def dataItemParser(str):
    # wl = str.split()
    wl = filter(None,[word.strip(string.punctuation)
                 for word in re.split('\s| ; |, |\*|/.*?|/[.*|/].*?|=|:|\'',str) if not word.isdigit()
                 ])
    for ins,i in enumerate(wl):
        if '|' in i:
            res = i.split('|')
            wl[ins] = res[-1]
    return wl

# def contains_sublist(lst, sublst):
#     n = len(sublst)
#     return any((sublst == lst[i:i+n]) for i in xrange(len(lst)-n+1))

def contains_sublist(lst, sublst):
    n = len(sublst)
    if any((sublst == lst[i:i+n]) for i in xrange(len(lst)-n+1)):
        pass
    else:
        # print "no match!"

        # print str(l)+": "+str(lst) + "--->" + str(sublst)

        return -1

    for i in xrange(len(lst)-n+1):
        if sublst == lst[i:i+n]:
            t=0
            while t < i:
                # print lst(t)
                labels.append(0)
                # print "lst index:"+str(t)+"; "+ "lst val: "+ str(lst[t])
                t += 1
            while t < i + n:

                labels.append(1)
                # print "lst index:"+str(t)+"; "+ "lst val: "+ str(lst[t])
                t += 1
            while t < (len(lst)):
                labels.append(0)
                # print "lst index:"+str(t)+"; "+ "lst val: "+ str(lst[t])
                t += 1
    return 0


def postionInSentence(s, i, n=3):
    '''
    :param s:length of sentence
    :param i: index of the word in question
    :return: position in senwl {start, mid, end}
    '''
    if s == 1:
        return "start"
    elif s == 2:
        if i + 1 == 1:
            return "start"
        else:
            return "end"
    else:
        avg = s/float(n)
        out = []
        last = 0.0
        while last < s:
            out.append(int(last + avg))
            last += avg
        # print avg
        # print out
        if i < out[0]:

            return "start"
        elif i >= out[0] and i < out[1]:
            # print " in mid"
            return "mid"
        else:
            # print "in end"
            return "end"

def contextCheck(checkLst,senWl,i):
    # checkLst = filter(None,[ line.rstrip() for line in open(path) if ('#' not in line)])
    slen = len(senWl)
    if slen == 1:
        return False
    if i - 1 >= 0 and i - 1 <= slen - 1:
        if senWl[i - 1] in checkLst:
            return True
    if i + 1 >= 0 and i + 1 <= slen - 1:
        if senWl[i + 1] in checkLst:
            return True
    if i - 2 >= 0 and i - 2 <= slen - 1:
        if senWl[i - 2] in checkLst:
            return True
    if i + 2 >= 0 and i + 2 <= slen - 1:
        if senWl[i + 2] in checkLst:
            return True
    return False

def wordCheck(checkLst,w):
    # checkLst = filter(None,[ line.rstrip() for line in open(path) if ('#' not in line)])
    if w in checkLst:
        return True
    else:
        return False

def entailfeaturePrepare(path):
    entailSet = set()
    f = codecs.open(path,"r","utf-8")
    for i in f:
        s = i.rstrip().split('\t')
        if s[2] >= 0:
            s.pop()
            for t in s:
                u = re.sub('@R@','',t)
                g = u.split()
                for b in g:
                    entailSet.add(b)
    entailLst = [c for c in entailSet if c not in stop]
    return entailLst

def subjectivePrepare(path,tag):
    f = codecs.open(path,"r","utf-8")
    lst = []
    for i in f:
        s = i.rstrip().split()
        t = s[0].split('=')
        if t[1] == tag:
            g = s[2].split('=')
            lst.append(g[1])
    return lst

def polarityPrepare(path):
    f = codecs.open(path,"r","utf-8")
    dict = {}
    for i in f:
        s = i.rstrip().split()
        t = s[2].split('=')
        w = s[5].split('=')
        # print t
        # print w
        dict[t[1]] = w[1]
    return dict

def polarityCheck(dict,w):
    if w in dict:
        return dict[w]
    else:
        return None

def checkNpov(w):
    if w in npovdict:
        return True
    else:
        return False

def collaborFea(w):
    if w in npovdict:
        return npovdict[w]
    else:
        return 0

def featureGen30(senWl):
    wordnet_lemmatizer = WordNetLemmatizer()
    slen = len(senWl)
    sentences = parser.parse(senWl)
    sen = ""
    for line in sentences:
        for sentence in line:
            sen += str(sentence)
    sent = sd.convert_tree(sen)

    for i,w in enumerate(senWl):
        dict = {}
        # f1
        dict['Word'] = w
        #f2
        dict['Lemma'] = wordnet_lemmatizer.lemmatize(w)
        r = nltk.pos_tag([w])
        #f3
        dict['POS'] = r[0][1]
        #f4
        if (i - 1) >= 0 and (i - 1) <= slen - 1:
            rm1 = nltk.pos_tag([senWl[i-1]])
            dict['POS-1'] = rm1[0][1]
        else:
            dict['POS-1'] = None
        #f5
        if (i + 1) >= 0 and (i + 1) <= slen - 1:
            rp1 = nltk.pos_tag([senWl[i+1]])
            dict['POS+1'] = rp1[0][1]
        else:
            dict['POS+1'] = None
        #f6
        if (i - 2) >= 0 and (i - 2) <= slen - 1:
            rm2 = nltk.pos_tag([senWl[i-2]])
            dict['POS-2'] = rm2[0][1]
        else:
            dict['POS-2'] = None
        #f7
        if (i + 2) >= 0 and (i + 2) <= slen - 1:
            rp2 = nltk.pos_tag([senWl[i+2]])
            dict['POS+2'] = rp2[0][1]
        else:
            dict['POS+2'] = None
        #f8
        dict['Position in sentence'] = postionInSentence(slen,i)
        #f9
        dict['Hedge'] = wordCheck(HedgeLst,w)
        #f10
        dict['Hedge in context'] = contextCheck(HedgeLst, senWl,i)
        #f11
        dict['Factive verb'] = wordCheck(FactiveLst,w)
        #f12
        dict['Factive verb in context'] = contextCheck(FactiveLst, senWl,i)
        #f13
        dict['Assertive verb'] = wordCheck(AssertiveLst,w)
        #f14
        dict['Assertive verb in context'] = contextCheck(AssertiveLst,senWl,i)
        #f15
        dict['Implicative verb'] = wordCheck(ImplicativeLst,w)
        #f16
        dict['Implicative verb in context'] = contextCheck(ImplicativeLst,senWl,i)
        #f17
        dict['Report verb'] = wordCheck(ReportLst,w)
        #f18
        dict['Report verb in context'] = contextCheck(ReportLst,senWl,i)
        #f19
        dict['Entailment'] = wordCheck(entailLst,w)
        #f20
        dict['Entailment in context'] = contextCheck(entailLst,senWl,i)
        #f21
        dict['Strong subjective'] = wordCheck(StrongSubjLst,w)
        #f22
        dict['Strong subjective in context'] = contextCheck(StrongSubjLst,senWl,i)
        #f23
        dict['Weak subjective'] = wordCheck(WeakSubjLst,w)
        #f24
        dict['Weak subjective in context'] = contextCheck(WeakSubjLst,senWl,i)
        #f25
        dict['Polarity'] = polarityCheck(PolarityDict,w)
        #f26
        dict['Positive word'] = wordCheck(PosiveLst,w)
        #f27
        dict['Positive word in context'] = contextCheck(PosiveLst,senWl,i)
        #f28
        dict['Negative word'] = wordCheck(NegativeLst,w)
        #f29
        dict['Negative word in context'] = contextCheck(NegativeLst,senWl,i)
        #f30
        dict['Grammatical relation'] = sent[i][7]
        #f31
        dict['Bias lexicon'] = checkNpov(w)
        #f32
        dict['Collaborative feature'] = collaborFea(w)

### main function ###

gram5_train = open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/5gram-edits-train.tsv','r')
# gram5_train = open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/PalestinianTerrorists.txt','r')


# testCase_squareBracket.txt
# test = open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/test_false_bracket0digit_try3.txt','w')
# testsim = open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/test_false_bracket0digit_try3_sim.txt','w')
test_nline8 = codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/test_nline8.txt','w','utf-8')
labNoMat = codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/test_labelsNotMatch.txt','w','utf-8')
npovLst = codecs.open("/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/npov_words.txt","w","utf-8")

# good tuple num in training set
l=0

#feature prepare
# f19; fill entail set
stop = stopwords.words('english')
entailLst = entailfeaturePrepare('/Volumes/Seagate Backup Plus Drive/npov_paper_data/reverb_local_global/Resource0812/reverb_local_clsf_all.txt')
HedgeLst = filter(None,[ line.rstrip() for line in codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/bias_related_lexicons/hedges_hyland2005.txt','r','utf-8') if ('#' not in line)])
FactiveLst = filter(None,[ line.rstrip() for line in codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/bias_related_lexicons/factives_hooper1975.txt','r','utf-8') if ('#' not in line)])
AssertiveLst = filter(None,[ line.rstrip() for line in codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/bias_related_lexicons/assertives_hooper1975.txt','r','utf-8') if ('#' not in line)])
ImplicativeLst = filter(None,[ line.rstrip() for line in codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/bias_related_lexicons/implicatives_karttunen1971.txt','r','utf-8') if ('#' not in line)])
ReportLst = filter(None,[ line.rstrip() for line in codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/bias_related_lexicons/report_verbs.txt','r','utf-8') if ('#' not in line)])
StrongSubjLst = subjectivePrepare('/Volumes/Seagate Backup Plus Drive/npov_paper_data/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff','strongsubj')
WeakSubjLst = subjectivePrepare('/Volumes/Seagate Backup Plus Drive/npov_paper_data/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff','weaksubj')
PolarityDict = polarityPrepare('/Volumes/Seagate Backup Plus Drive/npov_paper_data/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff')
PosiveLst = filter(None,[ line.rstrip() for line in codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/opinion-lexicon-English/positive-words.txt','r','utf-8') if (';' not in line)])
NegativeLst = filter(None,[ line.rstrip() for line in codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/opinion-lexicon-English/negative-words.txt','r') if (';' not in line)])
sd = StanfordDependencies.get_instance(backend="subprocess")
os.environ['STANFORD_PARSER'] = '/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/'
os.environ['STANFORD_MODELS'] = '/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/'
parser = stanford.StanfordParser(model_path="/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")


npovdict = {}
labels = []
features = []
line_num = 0
# npovlist = []
start = timeit.timeit()
for line in gram5_train:
    line = line.decode('utf8')
    line = line.rstrip('\n')
    nline = line.split('\t')
    line_num += 1
    print line_num
    print nline
    if nline[3] == 'true':
        if not checkHttpOnly(nline[6], nline[7]):
            if not check5gram(nline[6]) and not check5gram(nline[7]):
                n = nline[6].strip(string.punctuation).lower()
                m = nline[7].strip(string.punctuation).lower()
                # m = nline[7].strip('.,/"=:<>').lower()
                if edit_distance(n, m)>=4:
                    if not brackets0digit(nline[6]) or not brackets0digit(nline[7]):
                        str1 = strippedNoSquBrac(nline[6]) # no {{ or <
                        str2 = strippedNoSquBrac(nline[7])
                        if not checkSquarBrac(str1,str2):

                            # test_nline8.write(nline[8])
                            # print nline[8]
                            st1 = strip_tags(nline[8])
                            # print st1
                            st2 = strip_http(st1)
                            # print st2
                            st3 = strippedNoSquBrac(st2)
                            st4 = squrBracParse(st3)
                            # test_nline8.write(' -------->  '+st4+'\n')
                            senWl = dataItemParser(st4)
                            et1 = strip_tags(nline[6])
                            et2 = strip_http(et1)
                            et3 = strippedNoSquBrac(et2)
                            # print str(l)+": "+ et3
                            et4 = squrBracParse(et3)
                            # print str(l)+ ": "+et4
                            editWl = dataItemParser(et4) #
                            #generate label list

                            va = contains_sublist(senWl,editWl)
                            if va == -1:
                                labNoMat.write(line+'\n')
                                # print nline[6]+' ----> '+nline[7]
                            else:
                                # final good tuple
                                l += 1
                                # calculate frequency
                                for w in editWl:
                                    if npovdict.has_key(w):
                                        npovdict[w] += 1
                                    else:
                                        npovdict[w] = 1
                                # write npov words to file

                                for key in npovdict:
                                    print >>npovLst, key
                                test_nline8.write(line+'\n')
                                # features generation
                                features = featureGen30(senWl)
end = timeit.timeit()
print end - start

print l
print len(labels)
print len(features)
print features[0:2]
fea = codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/npov-edits/features_lst','w','utf-8')
fea.write(features)



# test.close()
# testsim.close()
gram5_train.close()
test_nline8.close()
labNoMat.close()
fea.close()