# The problem is as follows:
# We have an array of ranges, where each element in the array is the starting
# and ending point in a range. We merge all overlapping ranges into one range.


def merge_ranges(ranges):
    # ranges_prime = []
    ranges = sorted(ranges, key=lambda x: x[0])
    index = 0
    while index < len(ranges):
        r = ranges[index]
        if index+1 < len(ranges) and r[1] >= ranges[index+1][0]:
            ranges[index:index+2] = [[r[0], max(r[1], ranges[index+1][1])]]
        else:
            index += 1
    return ranges

ranges = [[5, 13], [8, 19], [27, 39], [32, 41], [4, 15]]
ranges = sorted(ranges, key=lambda x: x[0])
ranges = [
            [min(x[0], y[0]), max(x[1], y[1])] for x in ranges
            for y in ranges
            if x != y and
            (x[0] in range(y[0], y[1]+1) or x[1] in range(y[0], y[1]+1))
        ]

ranges = sorted(ranges, key=lambda x: x[0])
print ranges

# ranges = [
#             [min(x[0], y[0]), max(x[1], y[1])] for x in ranges
#             for y in ranges
#             if x != y and
#             (x[0] in range(y[0], y[1]+1) or x[1] in range(y[0], y[1]+1))
#         ]
# ranges = set(sorted(ranges, key=lambda x: x[0]))
# print ranges

# ranges = [[5, 13], [8, 19], [1,4]]
# ranges = sorted(ranges, key=lambda x:x[0])


def merge_reduce(r, s):
    print r
    print s
    if r[1] >= s[0]:
        return [r[0], s[1]]
    else:
        return r, s

# print reduce(merge_reduce, ranges)
# merge_ranges(ranges)
# print merge_ranges([[5, 13], [8, 19]])# [[5, 19]]
# print merge_ranges([[27, 39], [32, 41], [5, 13], [8, 19]])#
# print merge_ranges([[5, 13], [8, 19],[27, 39], [32, 41], [4,15] ] )
