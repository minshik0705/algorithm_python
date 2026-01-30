import sys

input = sys.stdin.readline
n = int(input().strip())
A = list(map(int, input().split()))
x = int(input().strip())

seen = set()
count = 0

for a in A:
    # 이미 a의 보수를 본 적이 있다면 (a + b == x인 b가 seen에 있다면) 한 쌍 완성
    if x - a in seen:
        count += 1
    seen.add(a)

print(count)