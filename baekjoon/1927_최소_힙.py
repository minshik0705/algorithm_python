import sys
from heapq import heappush, heappop
heap = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    cmd = int(sys.stdin.readline().strip())
    if heap:
        if cmd == 0:
            print(heappop(heap))
        else:
            heappush(heap, cmd)
    else:
        if cmd == 0:
            print(0)
        else:
            heappush(heap, cmd)