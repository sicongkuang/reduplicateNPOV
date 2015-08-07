__author__ = 'wxbks'
import re
import string
def a(test_str):
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

def check5gram(str):
    t = len(editsWordsList(a(str)))
    if t <= 5:
        print t
        return False
    else:
        return True

def editsWordsList(str):
    '''
        return list of words in the string
    '''
    wordl = []
    # wordl = re.compile('\w+').findall(str.strip('.,/"=:<>').lower())
    wordl = filter(None,[word.strip(string.punctuation)
                 for word in str.replace(';','; ').split()
                 ])
    print wordl
    return wordl

def brackets0digit(str):
    # ln = editsWordsList(a(str))
    str = a(str)
    wordl = filter(None,[word.strip(string.punctuation)
                 for word in str.replace(';','; ').split() if not word.isdigit()
                 ])
    if len(wordl) == 0:
        return True
    else: return False

w = ['2006]</ref>}}',   '2006]{{dead link|date=November 2011}}</ref>}}']
#
# w = ['mischaracterized',   'mischaracterized{{weasel-word|date=December 2008}}']
#
# w = ['{{Fact|date=December 2008}}',   '<ref>http://thomas.loc.gov/cgi-bin/bdquery/z?d110:SN2205:</ref>']
#
# w=['==Current status=={{Refimprove|date=February 2009}}',   '==2009 re-introduction==']
#
# w= ['gov/cgi-bin/query/F?c111:1:./temp/~c111OazjGv:e1560:</ref>,',   'gov/cgi-bin/query/z?c111:S.729:</ref>']
#
# w = ['Senate[[http://en.wikipedia.org/wiki/Senate]],',   '[[Senate]],']
#
# Senate,,   Senate[[http://en.wikipedia.org/wiki/Senate]],
#
# w=['a<b>c[d][[e]]f{g}t{{h}}i', 'f']
# w= ['£50,000.00 (worth today £1,270,000.00).','£50,000 (approximately £1.27&nbsp;million in 2010).']

# print check5gram(a(w[0]))

# print check5gram(a(w[1]))
print brackets0digit(w[0])
print brackets0digit(w[1])