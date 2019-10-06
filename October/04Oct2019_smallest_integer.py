"""
You are given an array of integers.
Return the smallest positive integer that is not present in the array.
The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2
because it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.
"""


def first_missing_positive(nums):
    index = 0
    for i in nums:
        if i <= 0:
            nums.remove(i)

    for i in range(0, len(nums)):
        val = abs(nums[i])
        if val-1 < len(nums):
            nums[val-1] = -nums[val-1]

    for i in nums:
        if i > 0:
            index = nums.index(i)

    return index+1


print(first_missing_positive([3, 4, -1, 1]))
# 2
