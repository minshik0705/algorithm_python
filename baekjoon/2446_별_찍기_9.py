import sys 
N = int(sys.stdin.readline().strip())

for i in range(2 * N - 1):
    if i < N:
        print(' ' * i + '*' * (2 * (N - i) - 1))
    else:
        print(' ' * (2 * (N - 1) - i) + '*' * (2 * (i - N + 1) + 1))