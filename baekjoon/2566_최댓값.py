import sys
arr = []
for i in range(9):
    arr.append(list(map(int, sys.stdin.readline().strip().split(' '))))
max_num = -1
idx = (1,1)
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num:
            max_num = arr[i][j]
            idx = (i+1, j+1)
print(max_num)
print(idx[0], idx[1])