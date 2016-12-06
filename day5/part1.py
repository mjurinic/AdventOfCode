import sys
import hashlib

def findPassword(doorId):
    ret = ""
    index = 0

    for i in xrange(8):
        while True:
            currHash = hashlib.md5(doorId + str(index)).hexdigest()

            if currHash[:5] == "00000":
                ret += currHash[5]
                index += 1
                break

            index += 1

    return ret

if __name__ == "__main__":
    doorId = sys.stdin.readline().strip()
    print findPassword(doorId)
