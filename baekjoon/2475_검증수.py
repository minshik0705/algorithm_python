import sys
numbers = list(map(int, sys.stdin.readline().strip().split(' ')))
tot = 0
for num in numbers:
    tot += num ** 2
print(tot % 10)