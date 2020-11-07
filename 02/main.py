import sys

DEBUG = True


def debug(x):
    if DEBUG:
        print(x.__str__())


# 1行目
n = int(input())

# 2行目以降
r = []
for l in sys.stdin:
    r.append(int(l))
debug(r)

result = r[1] - r[0]
size = len(r)

for i, ri in enumerate(r[0:size - 1]):
    debug('\nRi = ' + ri.__str__())
    for rj in r[1 + i:size]:
        debug('Rj = ' + rj.__str__())
        current = rj - ri
        debug('Rj - Ri = ' + current.__str__())
        if current > result:
            result = current

print(result)
