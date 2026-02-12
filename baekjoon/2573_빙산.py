import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ice_map = [list(map(int, input().split())) for _ in range(N)]

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 현재 빙산 칸만 저장 (최대 10,000개)
ice_cells = []
for y in range(N):
    for x in range(M):
        if ice_map[y][x] > 0:
            ice_cells.append((y, x))

visited = [[0] * M for _ in range(N)]
stamp = 0

def bfs(sy, sx):
    q = deque([(sy, sx)])
    visited[sy][sx] = stamp

    while q:
        y, x = q.popleft()
        for dy, dx in DIR:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] != stamp and ice_map[ny][nx] > 0:
                    visited[ny][nx] = stamp
                    q.append((ny, nx))

years_past = 0

while True:
    # 1) 덩어리 개수 체크 (빙산 칸 리스트만)
    if not ice_cells:
        print(0)
        break

    stamp += 1
    components = 0

    for y, x in ice_cells:
        if visited[y][x] != stamp:
            bfs(y, x)
            components += 1
            if components >= 2:
                print(years_past)
                sys.exit(0)

    # 2) 1년 녹이기 (빙산 칸만)
    melts = [0] * len(ice_cells)

    for i, (y, x) in enumerate(ice_cells):
        sea = 0
        for dy, dx in DIR:
            ny = y + dy
            nx = x + dx
            if ice_map[ny][nx] == 0:
                sea += 1
        melts[i] = sea

    new_cells = []
    for i, (y, x) in enumerate(ice_cells):
        nh = ice_map[y][x] - melts[i]
        if nh < 0:
            nh = 0
        ice_map[y][x] = nh
        if nh > 0:
            new_cells.append((y, x))

    ice_cells = new_cells
    years_past += 1
