import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(y, x):
    visited[y][x] = True
    
    sheep = 0
    wolves = 0
    
    if field[y][x] == 'o':
        sheep = 1
    elif field[y][x] == 'v':
        wolves = 1
    
    for dy, dx in DIR:
        ny = y + dy
        nx = x + dx
        
        if 0 <= ny < R and 0 <= nx < C:
            if not visited[ny][nx] and field[ny][nx] != '#':
                s, w = dfs(ny, nx)
                sheep += s
                wolves += w
    
    return sheep, wolves
    

R, C = map(int, input().split())

field = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
tot_sheep = tot_wolves = 0

for y in range(R):
    for x in range(C):
        if not visited[y][x] and field[y][x] != '#':
            sheep, wolves = dfs(y, x)
            if sheep > wolves:
                tot_sheep += sheep
            else:
                tot_wolves += wolves
print(tot_sheep, tot_wolves)