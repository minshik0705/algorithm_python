import sys
from collections import deque

input = sys.stdin.readline

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(sy, sx, field, visited):
    visited[sy][sx] = True
    q = deque([(sy, sx)])
    
    while q:
        y, x = q.popleft()
        for dy, dx in DIR:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W:
                if field[ny][nx] == '#' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

T = int(input().strip())

for _ in range(T):
    answer = 0
    field = []
    H, W = map(int, input().split())
    visited = [[False] * W for _ in range(H)]
    
    for _ in range(H):
        field.append(list(input().strip()))
        
    for y in range(H):
        for x in range(W):
            if field[y][x] == '#' and not visited[y][x]:
                answer += 1
                bfs(y, x, field, visited)
    print(answer)