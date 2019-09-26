"""
You are given an array of intervals - that is, an array of tuples (start, end).
The array may not be sorted, and could contain overlapping intervals.
Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

"""


def merge(intervals):
    counter = []
    count = -1
    for i in range(len(intervals)):
        count += 1
        for j in range(i+1, len(intervals)):
            if intervals[i][0] > intervals[j][0] and intervals[i][1] < intervals[j][1]:
                counter.append(count)
    for i in counter:
        del intervals[i]

    return intervals


print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
