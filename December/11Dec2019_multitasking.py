"""
We have a list of tasks to perform, with a cooldown period.
We can do multiple of these at the same time, but we cannot run the same task simultaneously.

Given a list of tasks, find how long it will take to complete the tasks in the order they are input.

tasks = [1, 1, 2, 1]
cooldown = 2
output: 7 (order is 1 _ _ 1 2 _ 1)
"""


def find_time(arr, cooldown):
    data = list()
    for i in range(0, len(arr)):
        if i == 0:
            update_list(data, arr[i])
        elif i == 1:
            if arr[i] == arr[i-1]:
                update_list(data, 0)
                update_list(data, 0)
                update_list(data, arr[i])
        else:
            first = arr[i-2]
            second = arr[i-1]

            if arr[i] != second:
                if arr[i] != first:
                    update_list(data, arr[i])
                else:
                    update_list(data, 0)
                    update_list(data, arr[i])
            else:
                update_list(data, 0)
                update_list(data, 0)
                update_list(data, arr[i])

    return len(data)


def update_list(data, num):
    data.append(num)


print(find_time([1, 1, 2, 1, 1, 2, 2, 2, 1], 2))
# 7
