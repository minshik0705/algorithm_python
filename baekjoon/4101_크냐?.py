import sys
while True:
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    if a == b and  a == 0:
        break
    if a>b:
        print('Yes')
    else:
        print('No')