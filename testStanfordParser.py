# -*- coding: utf-8 -*-
__author__ = 'wxbks'
import json
import os
from nltk.parse import stanford
import StanfordDependencies
import re
from zhon import hanzi
import zhon
# import Tkinter
import codecs
import re
import unicodedata

LHan = [[0x2E80, 0x2E99],    # Han # So  [26] CJK RADICAL REPEAT, CJK RADICAL RAP
        [0x2E9B, 0x2EF3],    # Han # So  [89] CJK RADICAL CHOKE, CJK RADICAL C-SIMPLIFIED TURTLE
        [0x2F00, 0x2FD5],    # Han # So [214] KANGXI RADICAL ONE, KANGXI RADICAL FLUTE
        0x3005,              # Han # Lm       IDEOGRAPHIC ITERATION MARK
        0x3007,              # Han # Nl       IDEOGRAPHIC NUMBER ZERO
        [0x3021, 0x3029],    # Han # Nl   [9] HANGZHOU NUMERAL ONE, HANGZHOU NUMERAL NINE
        [0x3038, 0x303A],    # Han # Nl   [3] HANGZHOU NUMERAL TEN, HANGZHOU NUMERAL THIRTY
        0x303B,              # Han # Lm       VERTICAL IDEOGRAPHIC ITERATION MARK
        [0x3400, 0x4DB5],    # Han # Lo [6582] CJK UNIFIED IDEOGRAPH-3400, CJK UNIFIED IDEOGRAPH-4DB5
        [0x4E00, 0x9FC3],    # Han # Lo [20932] CJK UNIFIED IDEOGRAPH-4E00, CJK UNIFIED IDEOGRAPH-9FC3
        [0xF900, 0xFA2D],    # Han # Lo [302] CJK COMPATIBILITY IDEOGRAPH-F900, CJK COMPATIBILITY IDEOGRAPH-FA2D
        [0xFA30, 0xFA6A],    # Han # Lo  [59] CJK COMPATIBILITY IDEOGRAPH-FA30, CJK COMPATIBILITY IDEOGRAPH-FA6A
        [0xFA70, 0xFAD9],    # Han # Lo [106] CJK COMPATIBILITY IDEOGRAPH-FA70, CJK COMPATIBILITY IDEOGRAPH-FAD9
        [0x20000, 0x2A6D6],  # Han # Lo [42711] CJK UNIFIED IDEOGRAPH-20000, CJK UNIFIED IDEOGRAPH-2A6D6
        [0x2F800, 0x2FA1D],# Han # Lo [542] CJK COMPATIBILITY IDEOGRAPH-2F800, CJK COMPATIBILITY IDEOGRAPH-2FA1D
        [0x2100, 0x214F]]
       # [0x1200,0x137F]]
def build_re():
    L = []
    for i in LHan:
        if isinstance(i, list):
            f, t = i
            try:
                f = unichr(f)
                t = unichr(t)
                L.append('%s-%s' % (f, t))
            except:
                pass # A narrow python build, so can't use chars > 65535 without surrogate pairs!

        else:
            try:
                L.append(unichr(i))
            except:
                pass

    RE = '[%s]' % ''.join(L)
    # print 'RE:', RE.encode('utf-8')
    return re.compile(RE, re.UNICODE)



# try:
#     all_chars = (unichr(i) for i in xrange(0x110000))
# except:
#     all_chars = (unichr(i) for i in xrange(0x10000))
# # control_chars = ''.join(c for c in all_chars if unicodedata.category(c) == 'Cc')
# # or equivalently and much more efficiently
# control_chars = ''.join(map(unichr, range(0,32) + range(127,160)))
#
# control_char_re = re.compile('[%s]' % re.escape(control_chars))
#
# def remove_control_chars(s):
#     return control_char_re.sub('', s)


## filter out letterlike symbols


# sd = StanfordDependencies.get_instance(backend="subprocess",version='2.0.4',jar_filename = '/Users/wxbks/Downloads/stanford-parser-2012-11-12/')
sd = StanfordDependencies.get_instance(backend="subprocess",version='3.4.1')
os.environ['STANFORD_PARSER'] = '/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/'
os.environ['STANFORD_MODELS'] = '/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/'

parser = stanford.StanfordParser(model_path="/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

# os.environ['STANFORD_PARSER'] = '/Users/wxbks/Downloads/stanford-parser-2012-11-12/'
# os.environ['STANFORD_MODELS'] = '/Users/wxbks/Downloads/stanford-parser-2012-11-12/'
# parser = stanford.StanfordParser()
# parser = stanford.StanfordParser(model_path="/Users/wxbks/Downloads/stanford-parser-2012-11-12/stanford-parser-2.0.4-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
# lst = ["what","I", "love", "you",u"Víctor"]
# lst = [u'Zoophilia', u'461109828', u'false', u'true', u'Plateau99', u'UNKNOWN',
#        u'zoophilia,', u'zoosexuality', u"jpg|thumb|right|300px|[[Hokusai]], Katsushika (\u845b\u98fe\u5317\u658e) (1760\u20131849) ''[[The Dream of the Fisherman's Wife]]'']]== Terminology ==There are three terms that are most commonly used in regards to the subject: zoophilia, bestiality, and zoosexuality.", u"jpg|thumb|right|300px|[[Hokusai]], Katsushika (\u845b\u98fe\u5317\u658e) (1760\u20131849) ''[[The Dream of the Fisherman's Wife]]'']]== Terminology ==There are three terms that are most commonly used in regards to the subject: bestiality, zoosexuality and zoophilia."]
# lst = [u'\u845b\u98fe\u5317\u658e']
# lst = [u'\u2111',u'August']
# lst=[u'\u845b\u98fe',u'\u845b\u98fe美e23',u'\u845b美e23']
# lst = ['August', 'In', 'just', 'the', 'fourth', 'meeting', 'of', 'pitcher]]s', 'with', 'the', 'same', 'last', 'name', 'since', '2000', 'V\xc3\xadctor', 'Zambrano', 'of', 'the', 'New', 'York', 'Mets', 'outdueled', 'Carlos', 'Zambrano', 'in', 'front', 'of', '40,321', 'fans', 'at', 'Shea', 'Stadium', 'pitching', 'the', 'New', 'York', 'Mets', 'to', 'a', '6\xe2\x80\x931', 'win', 'and', 'a', 'sweep', 'of', 'the', 'three-game', 'series']
# lst = [u'[[Hokusai', u'Katsushika', u'', u'1760\u20131849', u'The', u'Dream', u'of', u'the', u'Fisherman', u's', u'Wife', u'Terminology', u'There', u'are', u'three', u'terms', u'that', u'are', u'most', u'commonly', u'used', u'in', u'regards', u'to', u'the', u'subject', u'zoophilia', u'bestiality', u'and', u'zoosexuality']
# lst = [u'[[Hokusai', u'Katsushika', u'', u'1760\u20131849', u'The', u'Dream', u'of', u'the', u'Fisherman', u's', u'Wife', u'Terminology', u'There', u'are', u'three', u'terms', u'that', u'are', u'most', u'commonly', u'used', u'in', u'regards', u'to', u'the', u'subject', u'zoophilia', u'bestiality', u'and', u'zoosexuality']
# lst = [u'\u12a6\u122e\u121e', u'\u1361', u'\u1290\u133d\u1290\u1275\u1361', u'\u130d\u1295\u1263\u122d']
# lst = [u'\u12a6',u'\u1361']
# lst = [u'by', u'Pavel', u'Felgenhauer', u'\xabNovaya', u'gazeta\xbb', u'\u2116', u'August', u'14', u'2008']
# lst = [u'by', u'Pavel', u'Felgenhauer', u'\xabNovaya', u'gazeta\xbb', u'August', u'14', u'2008']
# lst = [u'OLF', u'symbolThe', u'Oromo', u'Liberation', u'Front', u'Oromo', u'Adda', u'Bilisummaa', u'Oromoo', u'Amharic', u'\u12a6\u122e\u121e', u'\u1361', u'\u1290\u133d\u1290\u1275\u1361', u'\u130d\u1295\u1263\u122d', u'or', u'OLF', u'is', u'an', u'organization', u'established', u'in', u'by', u'Oromo', u'nationalists', u'to', u'promote', u'self-determination', u'for', u'the', u'Oromo', u'people', u'against', u'Abyssinian', u'colonial', u'rule']

# print re.findall('[%s]' % zhon.hanzi.characters, 'I broke a plate: 我打破了一个盘子.')
lst = [u'\u1361',u'\u1290\u133d\u1290\u1275\u1361',u'\u130d\u1295\u1263\u122d']
# lst = ['tom','likes','to','eat','fish']

# for t,tv in enumerate(lst):
#     lst[t] = remove_control_chars(tv)
# print "one:"
# print lst

RE = build_re()
for i,ev in enumerate(lst):

    lst[i] = RE.sub('',ev)

print lst

lst = filter(None,[i for i in lst])
print lst
sentences = parser.parse(lst)

# sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your name?"))
# print sentences



# GUI
s=""
for line in sentences:
    for sentence in line:
        print str(sentence)
        s+=str(sentence)

try:
    sent = sd.convert_tree(s)
except AssertionError,e:
    pass


# for token in sent:
#     print token[7]
#
print "ok!!!!!!!!!"
for i,w in enumerate(lst):
    print "word:"+w
    print sent[i][7]

print len(lst)
print len(sent)



# NegativeLst = filter(None,[ line.rstrip() for line in codecs.open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/opinion-lexicon-English/negative-words.txt','r','utf-8') if (';' not in line)])
# filename = "/Users/wxbks/Downloads/test.txt"
# f = open(filename, 'r')
# for line in f:
#     line = line.decode('utf8')
#     line = line.rstrip('\n')
#     print line
#     nline = line.split('\t')
#     print nline