import sys
from itertools import combinations

input = sys.stdin.readline

def word2bit(word):
    bit = 0
    for char in word:
        bit |= (1 << (ord(char) - ord('a')))
    return bit

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]

if K < 5:
    print(0)
    sys.exit()

bits = [word2bit(word) for word in words]
base_bit = word2bit('antic')

if K == 26:
    print(N)
    sys.exit()

alphabet = [1 << i for i in range(26) if not (base_bit & (1 << i))]

answer = 0
for comb in combinations(alphabet, K - 5):
    know_bit = base_bit
    for b in comb:
        know_bit |= b

    count = 0
    for bit in bits:
        if (bit & know_bit) == bit:
            count += 1

    answer = max(answer, count)

print(answer)