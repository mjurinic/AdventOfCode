import sys
import re
import operator

NAME_REGEX = "([a-z-])+"
SECTOR_ID_REGEX = "([0-9])+"
CHECKSUM_REGEX = "\[([a-z0-9]+)\]"

def decrypt(room):
    checksum = re.search(CHECKSUM_REGEX, room).group(1)
    name = re.search(NAME_REGEX, room).group(0)

    charDict = {}

    for i in name:
        if i != '-':
            if i in charDict:
                charDict[i] = charDict[i] + 1
            else:
                charDict.update({i: 1})

    charList = sorted(charDict.items(), key = lambda x: (-x[1], x[0]))
    charList = [c[0] for c in charList[:5]]

    for c in checksum:
        if c not in charList:
            return 0

    return int(re.search(SECTOR_ID_REGEX, room).group(0))

if __name__ == "__main__":
    roomSum = 0

    for line in sys.stdin:
        roomSum += decrypt(line)

    print roomSum
