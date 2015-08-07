__author__ = 'wxbks'
import re
from nltk.parse import stanford
import StanfordDependencies
import os


replaceBlock = [[0x1200,0x137F],
                [0x0080,0x00FF]]



def replaceBlk():
    L = []
    for i in replaceBlock:
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


sd = StanfordDependencies.get_instance(backend="subprocess")

os.environ['STANFORD_PARSER'] = '/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/'
os.environ['STANFORD_MODELS'] = '/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/'

parser = stanford.StanfordParser(model_path="/Users/wxbks/Downloads/stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")



blk = replaceBlk()




# lst = [u'\u12a6\u122e\u121e', u'\u1361', u'\u1290\u133d\u1290\u1275\u1361', u'\u130d\u1295\u1263\u122d']
lst = [u'Ryke', u'Geerd', u'Hamer', u'born', u'May', u'1935', u'is', u'a', u'barred', u'German', u'physician', u'who', u'is', u'the', u'originator', u'of', u'the', u'Germanic', u'New', u'Medicine', u'\xae', u'also', u'formerly', u'known', u'as', u'German', u'New', u'Medicine', u'and', u'New', u'Medicine', u'an', u'highly', u'controversial', u'approach', u'to', u'illness', u'that', u'in', u'turn', u'criticizes', u'mainstream', u'medicine']
# lst = [u'\xae']
fakeLst = list(lst)
for i,ev in enumerate(fakeLst):

    fakeLst[i] = blk.sub(u'\u12a6',ev)

print "orin:" +str(lst)

print "new lst:" + str(fakeLst)
sentences = parser.parse(fakeLst)

s=""
for line in sentences:
    for sentence in line:
        s+=str(sentence)

sent = sd.convert_tree(s)

for i,w in enumerate(lst):
    print "word: %s , grammitcal relation: %s" % (lst[i],sent[i][7])
