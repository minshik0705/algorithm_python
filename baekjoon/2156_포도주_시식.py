import sys
n = int(sys.stdin.readline().strip())
wine = [int(sys.stdin.readline().strip()) for _ in range(n)]

if n == 1:
    print(wine[0])
    sys.exit()
if n == 2:
    print(wine[0] + wine[1])
    sys.exit()

dp = [0] * n
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(
    dp[1],                # 3번째 잔 건너뜀
    dp[0] + wine[2],      # (0) + (2)
    wine[1] + wine[2]     # (1) + (2)
)

for i in range(3, n):
    dp[i] = max(
        dp[i-1],                          # i번째 잔 건너뜀
        dp[i-2] + wine[i],                # i만 마심
        dp[i-3] + wine[i-1] + wine[i]     # i-1, i 마심 (i-2 건너뜀)
    )

print(dp[-1])
