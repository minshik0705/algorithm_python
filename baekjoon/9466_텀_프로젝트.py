import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def solve():
    T = int(input().strip())
    out_lines = []
    
    for _ in range(T):
        n = int(input().strip())
        pick = [0] + list(map(int, input().split()))
        
        visited = [False] * (n + 1)
        finished = [False] * (n + 1)
        
        team_count = 0
        
        def dfs(x):
            nonlocal team_count
            visited[x] = True
            nxt = pick[x]
            
            if not visited[nxt]:
                dfs(nxt)
            else:
                # nxt가 방문되었으나 아직 DFS 종료처리르 안했다면 -> 사이클
                if not finished[nxt]:
                    cur = nxt
                    cnt = 1
                    while cur != x:
                        cur = pick[cur]
                        cnt += 1
                    team_count += cnt
            
            finished[x] = True
        
        for i in range(1, n + 1):
            if not visited[i]:
                dfs(i)
                
        out_lines.append(str(n - team_count))
    
    print("\n".join(out_lines))
    
if __name__ == "__main__":
    solve()