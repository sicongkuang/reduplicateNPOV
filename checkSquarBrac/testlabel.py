__author__ = 'wxbks'

labels=[]
def contains_sublist(lst, sublst):
    n = len(sublst)
    if any((sublst == lst[i:i+n]) for i in xrange(len(lst)-n+1)):
        pass
    else:
        print "no match!"
        return

    for i in xrange(len(lst)-n+1):
        if sublst == lst[i:i+n]:
            t=0
            while t < i:
                # print lst(t)
                labels.append(0)
                print "lst index:"+str(t)+"; "+ "lst val: "+ str(lst[t])
                t += 1
            while t < i + n:

                labels.append(1)
                print "lst index:"+str(t)+"; "+ "lst val: "+ str(lst[t])
                t += 1
            while t < (len(lst)):
                labels.append(0)
                print "lst index:"+str(t)+"; "+ "lst val: "+ str(lst[t])
                t += 1

lst = ['i','love','you','you','are','son']
sublst = ['you','are']

lst1 = ['you','break','my','heart','and','i','will','not','forgive','you']
sublst1 = ['i','will','not']

contains_sublist(lst,sublst)
contains_sublist(lst1,sublst1)
print labels
print len(labels)


