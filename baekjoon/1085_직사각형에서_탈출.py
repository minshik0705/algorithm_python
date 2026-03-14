import sys
x, y, w, h = map(int, sys.stdin.readline().split(' '))
print(min(abs(x-w),abs(y-h), x, y))