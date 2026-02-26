import sys
from collections import deque

input = sys.stdin.readline

def is_bipartite(V, adj):
    color = [0] * (V + 1)  # 0: unvisited, 1 or -1: color

    for start in range(1, V + 1):
        if color[start] != 0:
            continue

        # start a BFS from this component
        color[start] = 1
        q = deque([start])

        while q:
            u = q.popleft()
            cu = color[u]

            for v in adj[u]:
                if color[v] == 0:
                    color[v] = -cu
                    q.append(v)
                elif color[v] == cu:
                    return False
    return True

def main():
    K = int(input().strip())
    out = []

    for _ in range(K):
        V, E = map(int, input().split())
        adj = [[] for _ in range(V + 1)]

        for _ in range(E):
            a, b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)

        out.append("YES" if is_bipartite(V, adj) else "NO")

    print("\n".join(out))

if __name__ == "__main__":
    main()