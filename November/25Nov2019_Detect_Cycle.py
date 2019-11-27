"""
Given a linked list, determine if the linked list has a cycle in it.
For notation purposes, we use an integer pos which represents the zero-indexed position where the tail connects to.

Example:
Input: head = [4,3,2,1,0], pos = 1.
Output: true
The example indicates a list where the tail connects to the second node.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        slow_p = head
        fast_p = head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True


testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail
testTail.next = node1

print(Solution().hasCycle(testHead))
# True
