import sys
from collections import deque

input = sys.stdin.readline

# 8 directions: 상하좌우 + 대각선
DIR8 = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]

def bfs(sy, sx, world, visited, h, w):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True

    while q:
        y, x = q.popleft()

        for dy, dx in DIR8:
            ny, nx = y + dy, x + dx

            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny][nx] and world[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    world = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0
    for y in range(h):
        for x in range(w):
            if world[y][x] == 1 and not visited[y][x]:
                bfs(y, x, world, visited, h, w)
                count += 1

    print(count)
