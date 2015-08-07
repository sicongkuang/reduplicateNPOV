__author__ = 'wxbks'
# -*- coding: utf-8 -*-

import string
import re
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

from HTMLParser import HTMLParser

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
                 for word in re.split('\s|;|,|\*|/|\[|\]|=|:|\'|',str) if not word.isdigit()
                 ])
    for ins,i in enumerate(wl):
        if '|' in i:
            res = i.split('|')
            wl[ins] = res[-1]
    return wl

s1="[[good]] er"
s2="[[good]] [[day]]"
# print checkSquarBrac(s1,s2)
# str="etc[e"
# str = "dfd|dfdf etr]] good[[day e <h1> * er * 3 ee]]ee </h1>eif/erj/ [[etc]]ere eke==eiru 39894 dfd 33 new[good day| goodgoodgood] [u|you yo!] [eu {good "
# str = "{{Spirituality portal}}The '''Transcendental Meditation''':youBeauty technique, or '''TM''', is a form of [[meditation]] that was introduced by [[Maharishi Mahesh Yogi]], an Indian spiritual teacher."
str = "<ref name=\"JVL2\"/> 	*10 August 1981: Palestinian terrorists threw two bombs at an Israeli embassy in [[Vienna]], wounding a 75-year old woman."
# str = "[http://times.hankooki.com/lpage/nation/200605/kt2006051218295711960.htm]==Redemption=={{see also|Parthenogenesis}}On August 2, 2007, after much independent investigation, it was revealed that the discredited South Korean scientist actually produced the first human embryos through parthenogenesis."
st1 = strip_tags(str)
print "st1:"+st1
st2 = strip_http(st1)
print "st2:"+st2
st3 = strippedNoSquBrac(st2)
st4 = squrBracParse(st3)
print st4
print dataItemParser(st4)
# print st3
# print st3.split()

