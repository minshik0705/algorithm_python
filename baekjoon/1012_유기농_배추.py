import sys
from collections import deque

input = sys.stdin.readline

def bfs(sx, sy, field, visited, M, N):
    q = deque([(sx, sy)])
    visited[sy][sx] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if field[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx, ny))




T = int(input().strip())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split(' '))
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split(' '))
        field[y][x] = 1
    count = 0
    
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                bfs(x, y, field, visited, M, N)
                count += 1
    print(count)    
