import sys

N = int(sys.stdin.readline().strip())

# N < 2면 소수 합으로 표현 불가
if N < 2:
    print(0)
    sys.exit(0)

# 에라토스테네스의 체
limit = N
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
p = 2
while p * p <= limit:
    if is_prime[p]:
        for x in range(p * p, limit + 1, p):
            is_prime[x] = False
    p += 1

primes = [i for i in range(2, limit + 1) if is_prime[i]]

# 투 포인터(슬라이딩 윈도우)
left = 0
right = 0
tot = 0
count = 0
L = len(primes)

while True:
    if tot >= N:
        if tot == N:
            count += 1
        tot -= primes[left]
        left += 1
    else:
        if right == L:
            break
        tot += primes[right]
        right += 1

print(count)