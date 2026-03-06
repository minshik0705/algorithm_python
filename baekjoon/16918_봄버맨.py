import sys
input = sys.stdin.readline

DIR = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]

def explode(grid, R, C):
    # 2초 상태: 전체 폭탄
    res = [['O'] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':  # 이 폭탄이 터지면
                for dr, dc in DIR:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        res[nr][nc] = '.'
    return res

def solve():
    R, C, N = map(int, input().split())
    initial = [list(input().strip()) for _ in range(R)]

    if N == 1:
        ans = initial
    elif N % 2 == 0:
        ans = [['O'] * C for _ in range(R)]
    else:
        A = explode(initial, R, C)   # N=3
        B = explode(A, R, C)         # N=5
        ans = A if N % 4 == 3 else B

    print('\n'.join(''.join(row) for row in ans))

if __name__ == "__main__":
    solve()