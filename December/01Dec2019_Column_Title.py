"""
MS Excel column titles have the following pattern: A, B, C, ..., Z,
AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc.
In other words, column 1 is named "A", column 2 is "B", column 26 is "Z",
column 27 is "AA" and so forth. Given a positive integer, find its corresponding column name.

Examples:
Input: 26
Output: Z

Input: 51
Output: AY

Input: 52
Output: AZ

Input: 676
Output: YZ

Input: 702
Output: ZZ

Input: 704
Output: AAB

"""


class Solution:
    def convertToTitle(self, n):
        string = [""] * 50
        print(string)

        # To store current index in str which is result
        i = 0

        while n > 0:
            # Find remainder
            rem = n % 26

            # if remainder is 0, then a
            # 'Z' must be there in output
            if rem == 0:
                string[i] = 'Z'
                i += 1
                n = (n / 26) - 1
            else:
                string[i] = chr(int((rem - 1) + ord('A')))
                i += 1
                n = n / 26
        string[i] = ''

        # Reverse the string and print result
        string = string[::-1]
        print("".join(string))


input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB
