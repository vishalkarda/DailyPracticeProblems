"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

"""


class Solution:
    # noinspection PyMethodMayBeStatic
    def min_sub_array_len(self, nums, s):
        mini = -1
        for i in range(0, len(nums)-1):
            if nums[i] == s:
                return 1
            total = nums[i]
            temp = 1
            for j in range(i+1, len(nums)):
                if total + nums[j] > s:
                    break

                temp += 1
                total += nums[j]

                if total == s:
                    if mini == -1:
                        mini = temp
                    elif mini > temp:
                        mini = temp
                    break

        return mini


print(Solution().min_sub_array_len([2, 3, 1, 2, 4, 3], 7))
# 2
