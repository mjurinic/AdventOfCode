import sys

cnt = []

def init(line):
    global cnt
    cnt = [{} for i in xrange(len(line))]

def process(line):
    global cnt

    for i in xrange(len(line)):
        if line[i] in cnt[i]:
            cnt[i][line[i]] = cnt[i][line[i]] + 1
        else:
            cnt[i].update({line[i]: 1})

def getErrorMsg():
    global cnt

    ret = ""

    for i in cnt:
        maxVal = float('Inf')
        bestChar = ''

        for key, value in i.items():
            if value < maxVal:
                bestChar = key
                maxVal = value

        ret += bestChar

    return ret

if __name__ == "__main__":
    first = True

    for line in sys.stdin:
        if first:
            init(line)
            first = False
        process(line)

    print getErrorMsg()
