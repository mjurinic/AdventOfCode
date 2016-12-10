import sys

def solve(line):
    sections = [s.split(']')[-1] for s in line.split('[')]
    hypernets = [s.split(']')[0] for s in line.split('[')][1:]

    ret = 0

    for section in sections:
        for i in xrange(3, len(section)):
            if section[i] == section[i - 3] and section[i - 1] == section[i - 2] and section[i] != section[i - 1]:
                ret = 1

    for hypernet in hypernets:
        for i in xrange(3, len(hypernet)):
            if hypernet[i] == hypernet[i - 3] and hypernet[i - 1] == hypernet[i - 2] and hypernet[i] != hypernet[i - 1]:
                return 0

    return ret

if __name__ == "__main__":
    print sum(solve(line.strip()) for line in sys.stdin.readlines())
