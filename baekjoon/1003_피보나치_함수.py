import sys

input = sys.stdin.readline

T = int(input().strip())
nums = [int(input().strip()) for _ in range(T)]
max_n = max(nums) if nums else 0

# zero[i], one[i] = f(i) 호출 중 f(0), f(1) 호출 횟수
zero = [0] * (max_n + 2)
one  = [0] * (max_n + 2)

zero[0], one[0] = 1, 0  # f(0)
zero[1], one[1] = 0, 1  # f(1)

for i in range(2, max_n + 1):
    zero[i] = zero[i-1] + zero[i-2]
    one[i]  = one[i-1]  + one[i-2]

for n in nums:
    print(zero[n], one[n])