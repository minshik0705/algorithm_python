import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(sy, sx, visited, colors):
    q = deque([(sy, sx)])
    visited[sy][sx] = True
    base = colors[sy][sx]

    while q:
        y, x = q.popleft()
        for dx, dy in DIR:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx] and colors[ny][nx] == base:
                    visited[ny][nx] = True
                    q.append((ny, nx))

def cvd_bfs(sy, sx, cvd_visited, colors):
    q = deque([(sy, sx)])
    cvd_visited[sy][sx] = True
    base = colors[sy][sx]

    while q:
        y, x = q.popleft()
        for dx, dy in DIR:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if cvd_visited[ny][nx]:
                    continue

                # 적록색약: R과 G를 같은 색으로 취급
                if base in ('R', 'G'):
                    if colors[ny][nx] in ('R', 'G'):
                        cvd_visited[ny][nx] = True
                        q.append((ny, nx))
                else:  # base == 'B'
                    if colors[ny][nx] == 'B':
                        cvd_visited[ny][nx] = True
                        q.append((ny, nx))

colors = []
for _ in range(N):
    colors.append(list(input().strip()))

visited = [[False] * N for _ in range(N)]
cvd_visited = [[False] * N for _ in range(N)]

count = 0
cvd_count = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(y, x, visited, colors)
            count += 1
        if not cvd_visited[y][x]:
            cvd_bfs(y, x, cvd_visited, colors)
            cvd_count += 1

print(count, cvd_count)
