import sys

input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# 끝나는 시간 -> 시작 시간 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = -1  # 시간은 0 이상이므로 -1로 시작하면 첫 회의도 안전하게 비교 가능
for s, e in meetings:
    if s >= end:     # 끝나자마자(동시에) 시작 가능하므로 >=
        cnt += 1
        end = e

print(cnt)