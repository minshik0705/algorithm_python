import sys

p ,q = map(int, sys.stdin.readline().strip().split(' '))
prime = []
for i in range(1, int(p ** (0.5) + 1)):
    if p % i == 0:
        prime.append(i)
        prime.append(p // i)
prime = list(set(prime))
prime.sort()
if q <= len(prime):
    print(prime[q - 1])
else:
    print(0)