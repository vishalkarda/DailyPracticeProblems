"""
You are given an array.
Each element represents the price of a stock on that particular day.
Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and
sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).

"""


def buy_and_sell(arr):
    maxi = 0
    mini = 0
    max_index = 0
    for i in range(len(arr)):
        # print(f'max index {max_index} max is {maxi} mini is {mini}')
        if max_index <= i:
            maxi = 0
        if arr[i] > maxi:
            maxi = arr[i]
            max_index = i
        if mini == 0:
            mini = arr[i]
        elif arr[i] < mini:
            mini = arr[i]
    # print(mini, maxi)
    return maxi-mini


print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
