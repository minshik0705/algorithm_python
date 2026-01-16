import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    q = deque((p, i) for i, p in enumerate(priorities))

    counts = [0] * 10  # 1~9
    for p in priorities:
        counts[p] += 1

    printed = 0

    while q:
        p, idx = q.popleft()

        # p보다 높은 중요도가 하나라도 남아있는지 체크
        if any(counts[h] > 0 for h in range(p + 1, 10)):
            q.append((p, idx))  # 뒤로 보내기
        else:
            printed += 1
            counts[p] -= 1
            if idx == M:
                print(printed)
                break