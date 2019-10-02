"""
You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
"""


# def matrix_spiral_print(M):
#     row = 0
#     col = 0
#     no_col = len(M[0])
#     no_row = len(M)
#     while True:
#         if row == 0 and col < no_col:
#             print(M[row][col], end=' ')
#             col += 1
#         else:
#             break
#     col -= 1
#     row = 1
#
#     while True:
#         if col == (no_col - 1) and row < no_row:
#             print(M[row][col], end=' ')
#             row += 1
#         else:
#             break
#     return 0
#
#
# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]
#
#
# matrix_spiral_print(grid)
# # 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12

data = [(1, 2), (5, 8), (4, 10), (20, 25)]

low = -1
high = 10**4
counter = -1
for value in data:
    if value[0] > low and value[1] < high:
        print(value)
        counter += 1
        low = value[0]
        high = value[1]
    else:
        low = value[0]
        high = value[1]

print(counter)
print([sorted(d) for d in data])
print(sorted([sorted(d) for d in data]))