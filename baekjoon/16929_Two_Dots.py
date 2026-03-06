import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
depth = [[0]*M for _ in range(N)]

DIR = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(y, x, py, px, d, color):
    visited[y][x] = True
    depth[y][x] = d

    for dy, dx in DIR:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < N and 0 <= nx < M):
            continue
        if board[ny][nx] != color:
            continue

        # 부모로 되돌아가는 간선은 무시
        if ny == py and nx == px:
            continue

        if visited[ny][nx]:
            # 이미 방문한 같은 색 정점을 다시 만났고,
            # 깊이 차이가 3 이상이면 (길이 >= 4 사이클)
            if d - depth[ny][nx] >= 3:
                return True
        else:
            if dfs(ny, nx, y, x, d + 1, color):
                return True

    return False

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if dfs(i, j, -1, -1, 0, board[i][j]):
                print("Yes")
                sys.exit(0)

print("No")