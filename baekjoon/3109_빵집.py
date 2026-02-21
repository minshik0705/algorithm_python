import sys
from collections import deque  # 네 스타일 유지용(실제로는 안 씀)

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

R, C = map(int, input().split())

# (오른쪽 위) -> (오른쪽) -> (오른쪽 아래)
DIR = [(1, -1), (1, 0), (1, 1)]

region = []
for _ in range(R):
    region.append(list(input().strip()))

visited = [[False] * C for _ in range(R)]

def dfs(x, y):
    if x == C - 1:
        return True

    for dx, dy in DIR:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < C and 0 <= ny < R:
            if region[ny][nx] == '.' and not visited[ny][nx]:
                visited[ny][nx] = True
                if dfs(nx, ny):
                    return True
    return False

cnt = 0
for y in range(R):
    if region[y][0] == '.' and not visited[y][0]:
        visited[y][0] = True
        if dfs(0, y):
            cnt += 1

print(cnt)