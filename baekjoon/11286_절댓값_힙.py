import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input().strip())

heap =[]


for _ in range(N):
    num = int(input().strip())
    if num != 0:
        heappush(heap, (abs(num), num))
    elif num == 0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)