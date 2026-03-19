import sys
input = sys.stdin.readline
INF = 10**15

N = int(input().strip())
W = [list(map(int, input().split())) for _ in range(N)]

start = 0
ALL = (1 << N) - 1

# dp[mask][u]를 딕셔너리/리스트로 관리해도 되고, 메모이제이션 재귀로 해도 됨
from functools import lru_cache

@lru_cache(None)
def tsp(mask, u):
    # 모든 도시 방문 완료 → start로 귀환
    if mask == ALL:
        return W[u][start] if W[u][start] > 0 else INF

    ans = INF
    # 다음 도시 v 탐색
    for v in range(N):
        if mask & (1 << v):  # 이미 방문
            continue
        if W[u][v] == 0:     # 길 없음
            continue
        cand = W[u][v] + tsp(mask | (1 << v), v)
        if cand < ans:
            ans = cand
    return ans

# 시작 도시에서 시작
print(tsp(1 << start, start))
