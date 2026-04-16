import heapq
import sys
N = int(sys.stdin.readline())
min_heap = []
max_heap = []

for _ in range(N):
  num = int(sys.stdin.readline())

  if not max_heap or num <= -max_heap[0]:
    heapq.heappush(max_heap, -num)
  else:
    heapq.heappush(min_heap, num)
  
  if len(max_heap) > len(min_heap) + 1:
    heapq.heappush(min_heap, -heapq.heappop(max_heap))
  elif len(min_heap) > len(max_heap):
    heapq.heappush(max_heap, -heapq.heappop(min_heap))

  if len(max_heap) == len(min_heap):
    mid = min(-max_heap[0], min_heap[0])
  else:
    mid = -max_heap[0]
  print(mid)