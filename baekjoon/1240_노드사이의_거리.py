import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

def dist_bfs(s, t):
    visited = [False] * (N + 1)
    q = deque([(s, 0)])
    visited[s] = True

    while q:
        cur, d = q.popleft()
        if cur == t:
            return d
        for nxt, w in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, d + w))
    return -1  # 트리라면 사실상 안 나옴

out = []
for _ in range(M):
    s, t = map(int, input().split())
    out.append(str(dist_bfs(s, t)))

print("\n".join(out))
