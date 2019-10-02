"""
Given two strings A and B of lowercase letters, return true if
and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false

"""


class Solution:

    def buddyStrings(self, A, B):

        if not A or not B or len(A) < 2 or len(B) < 2:
            return False

        elif len(A) == 2:
            temp = A[1]+A[0]
            return temp == B

        else:
            for i in range(0, len(A)):
                if A[i] != B[i]:
                    temp = A[:-2]+A[-1]+A[-2]
                    return temp == B


print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
