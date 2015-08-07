__author__ = 'wxbks'

#
# def contains_sublist(lst, sublst):
#     if not sublst:
#         for i in xrange(len(lst)):
#             labels.append(0)
#         return 0
#     print lst
#     print sublst
#     n = len(sublst)
#     m = len(lst)
#     if any((sublst == lst[i:i+n]) for i in xrange(m-n+1)):
#         print "come?"
#         pass
#     else:
#         # print "no match!"
#
#         # print str(l)+": "+str(lst) + "--->" + str(sublst)
#
#         return -1
#     print m-n+1
#     for i in xrange(m-n+1):
#         print labels
#         if sublst == lst[i:i+n]:
#             t=0
#             while t < i:
#                 # print lst(t)
#                 labels.append(0)
#                 # print "lst index:"+str(t)+"; "+ "lst val: "+ str(lst[t])
#                 t += 1
#             while t < i + n:
#
#                 labels.append(1)
#                 # print "lst index:"+str(t)+"; "+ "lst val: "+ str(lst[t])
#                 t += 1
#             while t < (len(lst)):
#                 labels.append(0)
#                 # print "lst index:"+str(t)+"; "+ "lst val: "+ str(lst[t])
#                 t += 1
#     return 0


def contains_sublist(lst, sublst):
    lst = filter(None, [one for one in lst])
    sublst = filter(None, [one for one in sublst])
    if not sublst:
        for i in xrange(len(lst)):
            labels.append((lst[i],0))
        return 0
    n = len(sublst)
    m = len(lst)
    if any((sublst == lst[i:i+n]) for i in xrange(m-n+1)):
        pass
    else:
        # print "no match!"

        # print str(l)+": "+str(lst) + "--->" + str(sublst)

        return -1

    d = [0] * len(lst)

    for i in xrange(m-n+1):
        if sublst == lst[i:i+n]:
            d[i:i+n] = [1] * n
    for k in zip(lst,d):
        labels.append(k)
    # labels.append(zip(lst,d))
    return 0

labels = []
senWl = ['i','k','t','k','t']
editWl = ['k','t']
# senWl = filter(None, [one for one in senWl])
# editWl = filter(None, [one for one in editWl])
res = contains_sublist(senWl,editWl)
senWl = ['i','k','t','k','t']
editWl = ['']
# senWl = filter(None, [one for one in senWl])
# editWl = filter(None, [one for one in editWl])
res = contains_sublist(senWl,editWl)
print res
print labels