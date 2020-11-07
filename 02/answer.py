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

minv = r[0]
for rj in r[1:size]:
    result = max(result, rj - minv)
    minv = min(minv, rj)

print(result)
