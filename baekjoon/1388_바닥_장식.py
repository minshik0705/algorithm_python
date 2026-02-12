import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

ans = 0

# 가로 판자: '-' 연속 구간 개수
for i in range(N):
    for j in range(M):
        if grid[i][j] == '-' and (j == 0 or grid[i][j - 1] != '-'):
            ans += 1

# 세로 판자: '|' 연속 구간 개수
for j in range(M):
    for i in range(N):
        if grid[i][j] == '|' and (i == 0 or grid[i - 1][j] != '|'):
            ans += 1

print(ans)
