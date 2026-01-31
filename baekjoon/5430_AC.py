import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cmd = input().strip()
    n = int(input())
    s = input().strip()

    # 배열 파싱
    if n == 0:
        dq = deque()
    else:
        dq = deque(map(int, s[1:-1].split(',')))

    rev = False
    error = False

    for c in cmd:
        if c == 'R':
            rev = not rev
        else:  # 'D'
            if not dq:
                error = True
                break
            if rev:
                dq.pop()
            else:
                dq.popleft()

    if error:
        print("error")
    else:
        if rev:
            dq.reverse()
        print("[" + ",".join(map(str, dq)) + "]")
