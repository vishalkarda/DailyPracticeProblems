# Definition for singly-linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        num = 0
        temp1 = l1
        temp2 = l2
        i = 1
        car = 0
        """(2 -> 4 -> 3) + (5 -> 6 -> 4)"""
        while temp1 and temp2:
            val = temp1.val + temp2.val + car
            if val > 10:
                num1 = val % 10
                car = val//10
            elif val == 10:
                num1 = 0
                car = 1
            else:
                num1 = val
                car = 0
            num += num1*i
            temp1 = temp1.next
            temp2 = temp2.next
            i *= 10

        res = num
        return res


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


result = Solution().addTwoNumbers(l1, l2)
print(result)
# while result:
#     print(result.val)
#     result = result.next
