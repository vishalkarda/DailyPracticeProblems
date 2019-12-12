"""
You are given a list of n numbers, where every number is at most k indexes
away from its properly sorted index.
Write a sorting algorithm (that will be given the number k) for this list that can solve this in O(n log k)

Example:
Input: [3, 2, 6, 5, 4], k=2
Output: [2, 3, 4, 5, 6]
As seen above, every number is at most 2 indexes away from its proper sorted index.
"""


def sort_partially_sorted(nums, k):
    for i in range(len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key

    return nums


print(sort_partially_sorted([3, 2, 6, 5, 4], 2))
# [2, 3, 4, 5, 6]
