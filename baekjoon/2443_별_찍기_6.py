import sys
N = int(sys.stdin.readline().strip())
for i in range(N):
    print(' ' * i, end = '')
    print('*' * (2 * (N - i) - 1)) 