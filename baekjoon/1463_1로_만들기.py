import sys

N = int(sys.stdin.readline())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    # 1을 빼는 경우
    best = dp[i - 1] + 1
    # 2로 나누는 경우(가능하면 비교)
    if i % 2 == 0:
        cand = dp[i // 2] + 1
        if cand < best:
            best = cand
    # 3으로 나누는 경우(가능하면 비교)
    if i % 3 == 0:
        cand = dp[i // 3] + 1
        if cand < best:
            best = cand
    dp[i] = best

print(dp[N])