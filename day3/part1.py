import sys

def isTriangle(a, b, c):
    tmpSum = 0
    tmpMax = a

    if tmpMax < b:
        tmpSum += tmpMax
        tmpMax = b
    else:
        tmpSum += b

    if tmpMax < c:
        tmpSum += tmpMax
        tmpMax = c
    else:
        tmpSum += c

    return 1 if tmpSum > tmpMax else 0

if __name__ == "__main__":
    cnt = 0

    for line in sys.stdin:
        sides = map(int, line.split())
        cnt += isTriangle(sides[0], sides[1], sides[2])

    print cnt
