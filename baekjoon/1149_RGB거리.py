#N= list(map(int,input().strip()))-> 해당 코드의 경우 한자리수는 처리를 못한다
import sys
input = sys.stdin.readline

N = int(input())
r, g, b = map(int, input().split())  # dp for house 1 (0-index 기준)

for _ in range(N - 1):
    cr, cg, cb = map(int, input().split())  # cost for current house
    nr = cr + min(g, b)  # 현재를 R로 칠하면 이전은 G/B 중 최소
    ng = cg + min(r, b)  # 현재 G → 이전 R/B
    nb = cb + min(r, g)  # 현재 B → 이전 R/G
    r, g, b = nr, ng, nb  # 다음 루프로 넘기기

print(min(r, g, b))