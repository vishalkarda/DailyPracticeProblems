"""
Given a binary tree, return all values given a certain height h.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


val = list()


def values_at_height(root, height):
    if root is None:
        return None

    if height == 1:
        val.append(root.value)
    else:
        values_at_height(root.left, height-1)
        values_at_height(root.right, height-1)

    return val


a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(values_at_height(a, 3))
# [4, 5, 7]
#     1
#    / \
#   2   3
#  / \   \
# 4   5   7
