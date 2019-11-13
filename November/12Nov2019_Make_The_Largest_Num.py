"""
Given a number of integers, combine them so it would create the largest number.

Example:
Input:  [17, 7, 2, 45, 72]
Output:  77245217
"""


# custom comparator to sort according
# to the ab, ba as mentioned in description
def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return (int(ba) > int(ab)) - (int(ba) < int(ab))


def myCompare(mycmp):
    # Convert a cmp= function into a key= function
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


# driver code
if __name__ == "__main__":
    a = [17, 7, 2, 45, 72]
    sorted_array = sorted(a, key=myCompare(comparator))
    number = "".join([str(i) for i in sorted_array])
    print(number)

# def largest_num(nums):
#     pass
#
#
# print(largest_num([17, 7, 2, 45, 72]))
# # 77245217
