import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

C = A ^ B
print(len(C))