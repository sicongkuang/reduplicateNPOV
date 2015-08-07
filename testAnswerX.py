__author__ = 'wxbks'

def answer1(x):
    if x<0:
        print "error:x should be 0 or greater"
        exit()
    if x>=2147483647:
        print "error:x should be less than 2^31 -1 (or 2147483647)"
        exit()
    s = str(x)
    l = len(s)
    if l==1:
        print "final x: %d" % x
        return x
    else:
        i=0
        sum = 0
        while i < l:
            d = int(s[i])
            sum = d + sum
            i += 1
            print "i:%d, sum:%d" % (d,sum)

        return answer(sum)


def answer(x):
    keyLst = []
    newX = set(x)
    # fal = newX.copy()
    newL = list(newX)
    flagL = [0]*len(newL)
    for ind,val in enumerate(newL):
        if val[::-1] in newL and flagL[ind] == 0:
            flagL[ind] = 1
            flagL[newL.index(val[::-1])]=1
            keyLst.append([val,val[::-1]])
        elif val[::-1] not in newL:
            keyLst.append([val])

    return len(keyLst)




# v =  answer1(21474836)
# print 'v:%d' % v
v= answer(["", "", ""])
print v