import sys
input = sys.stdin.readline

T = int(input().strip())

numbers = []
for _ in range(T):
    num = int(input().strip())
    numbers.append(num)

largest = max(numbers)

dp = [0] * (largest + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,largest + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(T):
    print(dp[numbers[i]])