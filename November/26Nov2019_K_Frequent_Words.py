"""
Given a non-empty list of words, return the k most frequent words.
The output should be sorted from highest to lowest frequency,
and if two words have the same frequency, the word with lower alphabetical order comes first. I
nput will contain only lower-case letters.

Example:
Input: ["daily", "interview", "pro", "pro",
"for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]
"""


# from collections import Counter


class Solution(object):

    def topKFrequent(self, words, k):
        res = sorted(set(words), key=lambda ele: words.count(ele), reverse=True)
        # res = [key for key, value in Counter(test_list).most_common()]
        return res[:k]


words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
