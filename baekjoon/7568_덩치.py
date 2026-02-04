import sys

N = int(sys.stdin.readline().strip())
people = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

ranks = []
for i in range(N):
    bigger = 0
    for j in range(N):
        if i == j:
            continue
        # 둘 다 엄격하게 커야 함 (동일하거나 한 쪽만 큰 경우는 카운트 안 함)
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            bigger += 1
    ranks.append(bigger + 1)

print(*ranks)
