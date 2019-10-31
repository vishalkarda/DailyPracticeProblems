"""
Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would be sorted.

Example:
Input: [1, 7, 9, 5, 7, 8, 10]
Output: (1, 5)
Explanation:
The numbers between index 1 and 5 are out of order and need to be sorted.
"""


def find_range(nums):
    n = len(nums)
    e = n - 1
    for s in range(0, n - 1):
        if nums[s] > nums[s + 1]:
            break

    if s == n - 1:
        exit()

    while e > 0:
        if nums[e] > nums[e - 1]:
            break
        e -= 1
    maxA = nums[s]
    minA = nums[s]

    for i in range(s + 1, e + 1):
        if nums[i] > maxA:
            maxA = nums[i]
        if nums[i] < minA:
            minA = nums[i]

    for i in range(s):
        if nums[i] > minA:
            s = i
            break

    i = n - 1
    while i >= e + 1:
        if nums[i] < maxA:
            e = i
            break
        i -= 1

    return s, e


print(find_range([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
