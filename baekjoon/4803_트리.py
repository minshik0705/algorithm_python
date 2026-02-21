import sys
from collections import deque

input = sys.stdin.readline

case = 1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    visited = [False] * (n + 1)
    trees = 0

    for start in range(1, n + 1):
        if visited[start]:
            continue

        q = deque([start])
        visited[start] = True

        nodes = 0
        deg_sum = 0  # 이 컴포넌트에서 degree 합 (나중에 /2 하면 간선 수)

        while q:
            v = q.popleft()
            nodes += 1
            deg_sum += len(g[v])

            for nv in g[v]:
                if not visited[nv]:
                    visited[nv] = True
                    q.append(nv)

        edges = deg_sum // 2
        if edges == nodes - 1:
            trees += 1

    if trees == 0:
        result = "No trees."
    elif trees == 1:
        result = "There is one tree."
    else:
        result = f"A forest of {trees} trees."

    print(f"Case {case}: {result}")
    case += 1