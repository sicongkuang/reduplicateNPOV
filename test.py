__author__ = 'wxbks'
import string
import re

def checkHttpLink(lst):
    '''
    return false if the list only contain urls
    :param str2: input the list of the difference
    :return:
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



w1 = ['][[Category:Pakistani painters]][[Category:People from Ludhiana]]',
 ']* [http://www.oldlahore.com/][[Category:Pakistani painters]][[Category:People from Ludhiana]]']
print checkHttpOnly(w1[0],w1[1])




w2 = ['[[Category:Pakistani painters]][[Category:Ludhiana]]',   '[[Category:Pakistani painters]][[Category:People from Ludhiana]]']
print checkHttpOnly(w2[0],w2[1])

w3 = ['asp?page=2009%5C02%5C15%5Cstory_15-2-2009_pg11_11]]',   'asp?page=2009%5C02%5C15%5Cstory_15-2-2009_pg11_11]']
print checkHttpOnly(w3[0],w3[1])

w4 = ['com/][[Category:Pakistani painters]][[Category:People from Ludhiana]]',   'com/]* [[http://www.nca.edu.pk/index.htm][[Category:Pakistani painters]][[Category:People from Ludhiana]]']
print checkHttpOnly(w4[0],w4[1])

w5 = ['Proponents of TM claim', 'Studies [http://tm.berkeley.edu/science.html] indicate']
print checkHttpOnly(w5[0],w5[1])

w6 = ['conservative-led','[http://www.gmconline.org/index.php?option=com_content&task=view&id=9&Itemid=14']
print checkHttpOnly(w6[0],w6[1])

w7 =['[2] </i>','</i>[[http://www.ushmm.org/museum/exhibit/online/jasenovac/]]']
print checkHttpOnly(w7[0],w7[1])

w8 = ['ref name="skeptic.com"/><ref name="popularmechanics.com"/>','<ref>http://www.skeptic.com/eskeptic/06-09-11</ref><ref>http://www.popularmechanics.com/science/defense/1227842.html?page=3</ref>']
print checkHttpOnly(w8[0],w8[1])

w9 = ['Senate[[http://en.wikipedia.org/wiki/Senate]]','[[Senate]]']
print checkHttpOnly(w9[0],w9[1])