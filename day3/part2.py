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
    sides = map(int, sys.stdin.read().split())

    cnt = i = 0

    while i < xrange(len(sides)):
        if i != 0 and i % 3 == 0:
            i += 6

        if i >= len(sides):
            break

        cnt += isTriangle(sides[i + 0], sides[i + 3], sides[i + 6])
        i += 1

    print cnt
