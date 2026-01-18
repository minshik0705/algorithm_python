import sys

n = int(sys.stdin.readline())
start = max(1, n - 9 * len(str(n)))  # 검증된 하한
answer = 0

for m in range(start, n):  # 생성자는 항상 N보다 작음
    s = m
    x = m
    while x > 0:
        s += x % 10
        x //= 10
    if s == n:
        answer = m
        break

print(answer)