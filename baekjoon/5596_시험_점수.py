import sys

minguk = list(map(int, sys.stdin.readline().split(' ')))
manguk = list(map(int, sys.stdin.readline().split(' ')))
print(max(sum(minguk), sum(manguk)))