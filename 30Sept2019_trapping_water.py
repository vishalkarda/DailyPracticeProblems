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
    left = mid = right = counter = 0
    for i in range(0, len(arr)):
        if i == 0:
            continue

        if i+1 < len(arr):
            print(f'left {arr[i - 1]} mid {arr[i]} right {arr[i + 1]}')
            left = arr[i-1]
            mid = arr[i]
            right = arr[i+1]

        if mid < left and mid < right:
            counter += 1

    return counter


print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
