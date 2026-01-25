import sys
N, M = map(int, sys.stdin.readline().strip().split(' '))
arr1 = []
arr2 = []
arr = [[0] * M for _ in range(N)]

for k in range(2):
    for i in range(N):
        if k == 0:
            arr1.append(sys.stdin.readline().strip().split(' '))
        elif k == 1:
            arr2.append(sys.stdin.readline().strip().split(' '))


for i in range(N):
    for  j in range(M):
        arr[i][j] = int(arr1[i][j]) + int(arr2[i][j])


for i in range(N):
    for j in range(M):
        print(arr[i][j], end = ' ')
    print()
