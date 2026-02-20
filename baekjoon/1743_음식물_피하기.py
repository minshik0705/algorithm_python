import sys
from collections import deque

input = sys.stdin.readline

DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]

N, M, K = map(int, input().split())

hallway = [[0] * M for _ in range(N)]

visited = [[False] * M for _ in range(N)]

answer = []

def bfs(sy, sx, hallway, visited):
    visited[sy][sx] = True
    size = 1
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for dy, dx in DIR:
            nx = x + dx
            ny = y + dy
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and hallway[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny))
                    size += 1
    return size

for _ in range(K):
    r, c = map(int, input().split())
    hallway[r - 1][c - 1] = 1

for y in range(N):
    for x in range(M):
        if hallway[y][x] == 1 and not visited[y][x]:
            answer.append(bfs(y, x, hallway, visited))
            
print(max(answer))