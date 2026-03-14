import sys
from collections import Counter
N = int(sys.stdin.readline().strip())
counter = Counter(bin(N))
print(counter['1'])