import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

# Create adjacency matrix
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

# Visited lists for DFS and BFS
visited1 = [0] * (N + 1)
visited2 = [0] * (N + 1)

# DFS Function
def dfs(V):
    visited1[V] = 1
    print(V, end=' ')
    for i in range(1, N + 1):
        if graph[V][i] == 1 and not visited1[i]:
            dfs(i)

# BFS Function (Optimized with deque)
def bfs(V):
    queue = deque([V])  # Using deque for efficient pops
    visited2[V] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, N + 1):
            if graph[v][i] == 1 and not visited2[i]:
                queue.append(i)
                visited2[i] = 1

# Execute DFS and BFS
dfs(V)
print()
bfs(V)