import sys

N, M = map(int, sys.stdin.readline().split())  # N: rows, M: cols
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

# 기준 패턴: (0,0)이 'W'인 8x8
ref = [['W' if (r + c) % 2 == 0 else 'B' for c in range(8)] for r in range(8)]

ans = 64  # 최댓값
for i in range(N - 7):
    for j in range(M - 7):
        mism = 0
        for r in range(8):
            for c in range(8):
                if board[i + r][j + c] != ref[r][c]:
                    mism += 1
        # W 시작 vs B 시작 중 최소
        ans = min(ans, mism, 64 - mism)

print(ans)