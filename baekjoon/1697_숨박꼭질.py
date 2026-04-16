import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    if K <= N:
        print(N - K)
        return

    MAX = 100000
    dist = [-1] * (MAX + 1)
    q = deque([N])
    dist[N] = 0

    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            return

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)

if __name__ == "__main__":
    solve()
