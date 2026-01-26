import sys
a, b, c = map(int, sys.stdin.readline().strip().split(' '))
arr = [a, b, c]
arr.sort()
print(arr[0], arr[1], arr[2])