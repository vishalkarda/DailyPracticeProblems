"""
Given a linked list of integers, remove all consecutive nodes that sum up to 0.
Example:
Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
Output: 10

The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed.
4 -> -4 also sums up to 0 too so that sequence should also be removed.
"""


class Node:
    """
    Node Class
    it represents the a singular node
    of a Linked List
    """
    def __init__(self, val, new=None):
        self.data = val
        self.next = new


def solution(nod):
    head = nod
    while nod.next:
        temp = nod
        som = 0
        while temp:
            som += temp.data
            if som == 0:
                head.next = temp.next
            temp = temp.next
        nod = nod.next
    return head


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node.next.next.next.next.next.next.next = Node(-4)

res = solution(node)
print(res.data)
print(res.next.data)


