"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library’s sort function for this problem.

Can you do this in a single pass?

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""


class Solution:
    def sortcolors(self, data):
        res = []
        zero_flag = False
        one_flag = False
        two_flag = False
        count_zero = 0

        for i in range(len(data)):
            if data[i] == 0 and zero_flag:
                res.insert(1, data[i])
                count_zero += 1
            if data[i] == 1 and one_flag:
                res.insert(2, data[i])
            if data[i] == 2 and two_flag:
                res.insert(len(res)-1, data[i])
            if data[i] == 0 and not zero_flag:
                res.insert(0, data[i])
                zero_flag = True
            if data[i] == 1 and not one_flag:
                res.insert(1, data[i])
                one_flag = True
            if data[i] == 2 and not two_flag:
                res.insert(2, data[i])
                two_flag = True
            print(f'new list {i} : {res}')
        return res


nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortcolors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
