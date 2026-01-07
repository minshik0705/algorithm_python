import sys, math

X = int(sys.stdin.readline().strip())

# d: T(d) = d(d+1)/2 >= X 를 만족하는 최소 d
d = math.ceil((-1 + math.sqrt(1 + 8*X)) / 2)

prev = d*(d-1)//2       # 직전 대각선까지의 누적 개수
pos = X - prev          # d번째 대각선 내 위치 (1-based)

if d % 2 == 0:
    num = pos
    den = d - pos + 1
else:
    num = d - pos + 1
    den = pos

print(f"{num}/{den}")