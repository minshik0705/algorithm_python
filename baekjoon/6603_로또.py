import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    numbers = list(map(int, input().split()))
    k = numbers[0]
    if k == 0:
        break

    S = numbers[1:]

    for comb in combinations(S, 6):
        print(*comb)
    print()
