__author__ = 'wxbks'


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
        print avg
        print out
        if i < out[0]:

            return "start"
        elif i >= out[0] and i < out[1]:
            # print " in mid"
            return "mid"
        else:
            # print "in end"
            return "end"

def contextCheck(path,senWl,i):
    checkLst = filter(None,[ line.rstrip() for line in open(path) if ('#' not in line)])
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

def wordCheck(path,w):
    checkLst = filter(None,[ line.rstrip() for line in open(path) if ('#' not in line)])
    if w in checkLst:
        return True
    else:
        return False

def split(a, n):
    k, m = len(a) / n, len(a) % n
    edge = []
    (edge.append((i * k + min(i, m),(i + 1) * k + min(i + 1, m))) for i in xrange(n))
    return edge

#
# def entailmentCheck(path,w):
#     f = open(path,"r")
#     entailList = []
#     for i in f:
#         s = i.rstrip().split('\t')
#         if s[2] > 0:


def subjectivePrepare(path,tag):
    f = open(path,"r")
    lst = []
    for i in f:
        s = i.rstrip().split()
        t = s[0].split('=')
        if t[1] == tag:
            g = s[2].split('=')
            lst.append(g[1])
    return lst

def polarityPrepare(path):
    f = open(path,"r")
    dict = {}
    for i in f:
        s = i.rstrip().split()
        t = s[2].split('=')
        w = s[5].split('=')
        # print t
        # print w
        dict[t[1]] = w[1]

    return dict

# print postionInSentence(7,4)
# list = []
# with open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/bias_related_lexicons/hedges_hyland2005.txt') as f:
#     lines = f.read().splitlines()
#
#     if '#' not in lines:
#         list.append(lines)
#
# print list
# lst = filter(None,[ line.rstrip() for line in open('/Volumes/Seagate Backup Plus Drive/npov_paper_data/bias_related_lexicons/hedges_hyland2005.txt') if ('#' not in line)])
#
# print len(lst)
#
# lst = subjectivePrepare('/Volumes/Seagate Backup Plus Drive/npov_paper_data/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff','strongsubj')
# print lst[5]

PolarityDict = polarityPrepare('/Volumes/Seagate Backup Plus Drive/npov_paper_data/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff')
print len(PolarityDict)