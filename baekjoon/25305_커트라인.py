import sys
people, cut = map(int, sys.stdin.readline().strip().split(' '))
rank = list(map(int, sys.stdin.readline().strip().split(' ')))
rank.sort(reverse = True)
print(rank[:cut:][-1])