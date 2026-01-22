import sys

input = sys.stdin.readline
n = int(input().strip())
scores = [0] + [int(input().strip()) for _ in range(n)]  # 1-index

if n == 1:
    print(scores[1])
elif n == 2:
    print(max(scores[2], scores[1] + scores[2]))
else:
    dp = [0] * (n + 1)
    dp[1] = scores[1]
    dp[2] = max(scores[2], scores[1] + scores[2])
    # dp[3]을 점화식으로 계산해도 되지만 명시적으로 적어둡니다.
    dp[3] = max(scores[1] + scores[3], scores[2] + scores[3])

    for i in range(4, n + 1):
        dp[i] = max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i])

    print(dp[n])
