import sys

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    last = pow(a, b, 10)   # (a^b) % 10 을 빠르게 계산
    print(10 if last == 0 else last)
