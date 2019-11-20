"""
Given the root of a binary tree, print its level-order traversal. For example:

  1
 / \
2   3
   / \
  4   5

The following tree should output 1, 2, 3, 4, 5.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_level_order(root):
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = list()

    # Enqueue Root and initialize height
    queue.append(root)

    while len(queue) > 0:
        # Print front of queue and remove it from queue
        print(queue[0].val, end=' ')
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

            # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5
