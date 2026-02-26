import sys
from collections import deque

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
input = sys.stdin.readline

width, length = map(int, input().split())

war_map = []
for _ in range(length):
    war_map.append(list(input().strip()))

visited = [[False] * width for _ in range(length)]  # [length][width]

def bfs(sy, sx, team):
    cnt = 1
    visited[sy][sx] = True
    q = deque([(sy, sx)])

    while q:
        y, x = q.popleft()
        for dy, dx in DIR:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < length and 0 <= nx < width:
                if not visited[ny][nx] and war_map[ny][nx] == team:
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((ny, nx))
    return cnt

war_power = {'W': 0, 'B': 0}

for y in range(length):
    for x in range(width):
        if not visited[y][x]:
            team = war_map[y][x]
            size = bfs(y, x, team)
            war_power[team] += size * size

print(war_power['W'], war_power['B'])
