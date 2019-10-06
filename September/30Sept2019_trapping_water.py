"""
You have a landscape, in which puddles can form.
You are given an array of non-negative integers representing the elevation at each location.
Return the amount of water that would accumulate if it rains.

For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
       X
   X███XX█X
 X█XX█XXXXXX
# [0,1,0,2,1,0,1,3,2,1,2,1]
"""


def capacity(arr):
    n = len(arr)
    # initialize output
    result = 0

    # maximum element on left and right
    left_max = 0
    right_max = 0

    # indices to traverse the array
    lo = 0
    hi = n - 1

    while lo <= hi:

        if arr[lo] < arr[hi]:

            if arr[lo] > left_max:

                # update max in left
                left_max = arr[lo]
            else:

                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo += 1

        else:

            if arr[hi] > right_max:
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi -= 1

    return result


print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
