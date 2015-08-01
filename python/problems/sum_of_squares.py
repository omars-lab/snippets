import math


def r2(X):
    if X == 0:
        return 1

    squares = [x**2 for x in range(0, int(math.floor(math.sqrt(X)))+1)]

    pairs = []
    for v in squares:
        if (X-v) > 0 and (X-v) in squares and ((min(X, v), max(X, v))
                                               not in pairs):
            pairs += [(min(X, v), max(X, v))]
    return len(pairs)*4


def sol(x):
    total = 0
    for x in range(0, x**2+1):
        total += r2(x)
    return total


for x in range(0, 13):
    print "index: %s, sum: %s" % (x, sol(x))
