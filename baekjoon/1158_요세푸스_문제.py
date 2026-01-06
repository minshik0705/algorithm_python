import sys

N, K = map(int, sys.stdin.readline().split())
people = list(range(1, N + 1))
result = []
idx = 0

while people:
    idx = (idx + K - 1) % len(people)  # 다음에 제거할 사람 위치
    result.append(people.pop(idx))     # 해당 사람 제거

print('<' + ', '.join(map(str, result)) + '>')