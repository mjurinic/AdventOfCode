import sys
import re
from string import ascii_lowercase

NAME_REGEX = "([a-z-])+"
SECTOR_ID_REGEX = "([0-9])+"
CHECKSUM_REGEX = "\[([a-z0-9]+)\]"

def decrypt(room):
    checksum = re.search(CHECKSUM_REGEX, room).group(1)
    name = re.search(NAME_REGEX, room).group(0)
    sectorId = int(re.search(SECTOR_ID_REGEX, room).group(0))

    realString = ""

    for c in name:
        tmpC = c

        if c != '-':
            for i in xrange(sectorId):
                tmpC = chr((ord(tmpC) - ord('a') + 1) % 26 + ord('a'))
        else:
            tmpC = ' '

        realString += tmpC

    return sectorId if "north" in realString else 0

if __name__ == "__main__":
    sol = 0

    for line in sys.stdin:
        sol += decrypt(line)

    print sol
