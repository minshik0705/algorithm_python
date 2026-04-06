import sys
from collections import deque

answer = 0

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
deq = deque(arr)
find = list(map(int, input().split()))

for num in find:
    length = len(deq)
    idx = deq.index(num)
    rot = min(idx, length - idx)
    answer += rot
    if rot == 0:
        deq.popleft()
    elif rot == idx:
        deq.rotate(-rot)
        deq.popleft()
    else:
        deq.rotate(rot)
        deq.popleft()

print(answer)
        