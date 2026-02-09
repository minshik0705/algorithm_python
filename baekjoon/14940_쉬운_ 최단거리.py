import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = []
sx = sy = -1

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j, v in enumerate(row):
        if v == 2:
            sx, sy = i, j

dist = [[-1] * m for _ in range(n)]
q = deque()

dist[sx][sy] = 0
q.append((sx, sy))

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            # 이동 가능한 땅(1)만 거리 갱신 대상
            if grid[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

# 출력 규칙 적용
out_lines = []
for i in range(n):
    line = []
    for j in range(m):
        if grid[i][j] == 0:
            line.append("0")
        else:
            line.append(str(dist[i][j]))
    out_lines.append(" ".join(line))

print("\n".join(out_lines))
