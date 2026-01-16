import sys
from collections import Counter
import math

input = sys.stdin.readline

N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]
arr.sort()

# 1) 산술평균: half-up 반올림 (음수 처리 주의)
s = sum(arr)
avg = s / N
if avg >= 0:
    mean = int(avg + 0.5)
else:
    mean = int(avg - 0.5)
print(mean)

# 2) 중앙값
print(arr[N // 2])

# 3) 최빈값 (동점이면 두 번째로 작은 값)
freq = Counter(arr)
max_cnt = max(freq.values())
candidates = [x for x, c in freq.items() if c == max_cnt]
candidates.sort()
mode = candidates[0] if len(candidates) == 1 else candidates[1]
print(mode)

# 4) 범위
print(arr[-1] - arr[0])