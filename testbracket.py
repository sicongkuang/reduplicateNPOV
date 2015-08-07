__author__ = 'wxbks'
import string
def brackets0digit(str):
    # ln = editsWordsList(a(str))
    str = stripped(str)
    print str
    wordl = filter(None,[word.strip(string.punctuation)
                 for word in str.replace(';','; ').split() if not word.isdigit()
                 ])
    if len(wordl) == 0:
        print wordl
        return True
    else:
        print wordl
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

# w = ['2006]</ref>}}',   '2006]{{dead link|date=November 2011}}</ref>}}']
# w = ['</math>:{{fact}},',   '</math>:{{fact|date=September 2012}}']
w=['{{fact}},',   '{{fact|date=September 2012}}']

# w = ['96.000,'   ,'2,000,000']
560,   40,000
2002, 3, 4,   2002/2003/2004

print brackets0digit(w[0])
print brackets0digit(w[1])
# print brackets0digit(w[0])

if not brackets0digit(w[0]) or not brackets0digit(w[1]):
    print 'this is good tuple'
else:
    print 'this is bad tuple'