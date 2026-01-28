import sys
a, b = map(str, sys.stdin.readline().split(' '))
A = int(a[-1::-1])
B = int(b[-1::-1])
print(max(A,B))