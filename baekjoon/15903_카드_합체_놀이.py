import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)

for _ in range(m):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    s = a + b
    heapq.heappush(cards, s)
    heapq.heappush(cards, s)

print(sum(cards))