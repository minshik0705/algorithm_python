import sys
from collections import deque

input = sys.stdin.readline

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

M, N, K = map(int, input().split())

blocked = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    
    for r in range(M - y2, M - y1):
        for c in range(x1, x2):
            blocked[r][c] = 1

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = 1
    area = 1
    
    while q:
        r, c = q.popleft()
        
        for dx, dy in DIR:
            nr = r + dy
            nc = c + dx
            
            if 0 <= nr < M and 0 <= nc < N:
                if visited[nr][nc] == 0 and blocked[nr][nc] == 0:
                    visited[nr][nc] = 1
                    area += 1
                    q.append((nr, nc))
    return area
    
areas = []

for r in range(M):
    for c in range(N):
        if blocked[r][c] == 0 and visited[r][c] == 0:
            areas.append(bfs(r, c))
            
areas.sort()
print(len(areas))
print(*areas)