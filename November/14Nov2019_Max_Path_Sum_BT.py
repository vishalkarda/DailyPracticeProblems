"""
You are given the root of a binary tree.
Find the path between 2 nodes that maximizes the sum of all the nodes in the path,
and return the sum. The path does not necessarily need to go through the root.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findMaxUtil(root):
    # Base Case
    if root is None:
        return 0

        # l and r store maximum path sum going through left
    # and right child of root respetively
    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)

    # Max path for parent call of root. This path
    # must include at most one child of root
    max_single = max(max(l, r) + root.val, root.val)

    # Max top represents the sum when the node under
    # consideration is the root of the maxSum path and
    # no ancestor of root are there in max sum path
    max_top = max(max_single, l + r + root.val)

    # Static variable to store the changes
    # Store the maximum result
    findMaxUtil.res = max(findMaxUtil.res, max_top)

    return max_single


def maxPathSum(root):
    findMaxUtil.res = float("-inf")

    # Compute and return result
    findMaxUtil(root)
    return findMaxUtil.res

# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4


root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(maxPathSum(root))
# 42