import sys
import hashlib

def findPassword(doorId):
    ret = ['' for i in xrange(8)]
    index = 0

    while '' in ret:
        while True:
            currHash = hashlib.md5(doorId + str(index)).hexdigest()

            if currHash[:5] == "00000":
                index += 1

                try:
                    if ret[int(currHash[5])] != '':
                        continue

                    ret[int(currHash[5])] = currHash[6]
                    break
                except:
                    continue

            index += 1

    return ''.join(ret)

if __name__ == "__main__":
    doorId = sys.stdin.readline().strip()
    print findPassword(doorId)
