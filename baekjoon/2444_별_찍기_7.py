import sys
N = int(sys.stdin.readline().strip())
for i in range(N, 0, -1):
    for j in range(i - 1):
        print(' ', end = '')
    for k in range(2*(N - i) + 1):
        print('*', end = '')
    print()

for i in range(N - 1):
    for j in range(i + 1):
        print(' ', end = '')
    for k in range(2 *(N - i - 1) - 1):
        print('*', end = '')
    print()