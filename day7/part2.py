import sys

def solve(line):
    supernets = [s.split(']')[-1] for s in line.split('[')]
    hypernets = [s.split(']')[0] for s in line.split('[')][1:]

    for hypernet in hypernets:
        for i in xrange(2, len(hypernet)):
            bab = hypernet[i] + hypernet[i - 1] + hypernet[i - 2]

            if bab[0] == bab[2]:
                aba = bab[1] + bab[0] + bab[1]

                if True in [aba in supernet for supernet in supernets]:
                    return 1

    return 0

if __name__ == "__main__":
    print sum(solve(line.strip()) for line in sys.stdin.readlines())
