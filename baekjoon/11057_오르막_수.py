import sys
input = sys.stdin.readline

MOD = 10007
N = int(input().strip())

dp = [1] * 10  # 길이 1: 마지막 숫자 0~9 각각 1개

for _ in range(2, N + 1):
    for d in range(1, 10):
        dp[d] = (dp[d] + dp[d - 1]) % MOD

print(sum(dp) % MOD)
