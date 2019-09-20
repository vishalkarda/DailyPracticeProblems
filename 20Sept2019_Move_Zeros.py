"""
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:

    def move_zeros(self, nums):
        # Fill this in.
        counter = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                counter += 1
            else:
                if i != 0:
                    temp = abs(i-counter)
                    nums[temp] = nums[i]
                    nums[i] = 0

        return nums


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0]
Solution().move_zeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

