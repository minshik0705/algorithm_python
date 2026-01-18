import sys
num = int(sys.stdin.readline().strip())
dp = [0] * (num + 1)
for i in range(num + 1):
    if i == 0:
        continue
    elif i == 1 or i == 2:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[-1])