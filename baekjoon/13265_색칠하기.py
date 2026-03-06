import sys
from collections import deque
input = sys.stdin.readline

def is_bipartite(n, graph):
    color = [-1] * (n + 1)  # -1: uncolored, 0/1: two colors

    for start in range(1, n + 1):
        if color[start] != -1:
            continue

        color[start] = 0
        q = deque([start])

        while q:
            u = q.popleft()
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True

def main():
    T = int(input().strip())
    for _ in range(T):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        print("possible" if is_bipartite(n, graph) else "impossible")

if __name__ == "__main__":
    main()