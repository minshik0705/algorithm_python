import sys
import heapq

input = sys.stdin.readline
INF = 10**18

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        cur_dist, now = heapq.heappop(pq)

        if cur_dist > dist[now]:
            continue

        for nxt, weight in graph[now]:
            new_dist = cur_dist + weight
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))   # 방향 그래프: u -> v

dijkstra(K)

for i in range(1, V + 1):
    print("INF" if dist[i] == INF else dist[i])