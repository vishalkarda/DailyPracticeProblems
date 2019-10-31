"""
Write a function that reverses the digits a 32-bit signed integer, x.
Assume that the environment can only store integers within the 32-bit signed integer range,
[-2^31, 2^31 - 1]. The function returns 0 when the reversed integer overflows.

Example:
Input: 123
Output: 321
"""


class Solution:

    def reverse(self, x):
        neg = False
        if x < 0:
            x = -x
            neg = True
        if x >= 2**31:
            return 0
        else:
            _list = list(str(x))
            _list_reverse = _list[::-1]
            res = int(''.join(_list_reverse))
            return -res if neg else res


print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
