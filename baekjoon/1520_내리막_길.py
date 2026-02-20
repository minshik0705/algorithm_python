import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]

dp = [[-1] * N for _ in range(M)]  # -1: 아직 계산 안 함

def dfs(y, x):
    # 도착점
    if y == M - 1 and x == N - 1:
        return 1

    # 이미 계산됨
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    cur_h = board[y][x]

    for dy, dx in DIR:
        ny, nx = y + dy, x + dx
        if 0 <= ny < M and 0 <= nx < N:
            if board[ny][nx] < cur_h:          # 내리막만
                dp[y][x] += dfs(ny, nx)

    return dp[y][x]

print(dfs(0, 0))
