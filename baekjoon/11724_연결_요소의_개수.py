import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(' '))

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)

def bfs(start: int):
    q = deque([start])
    visited[start] = True
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
count = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        count += 1
print(count)