import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = x1 - x2
    dy = y1 - y2
    d2 = dx*dx + dy*dy

    if d2 == 0:  # 중심이 같음
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue

    sum_r = r1 + r2
    diff_r = abs(r1 - r2)

    if d2 > sum_r * sum_r:
        print(0)
    elif d2 == sum_r * sum_r:
        print(1)
    elif d2 < diff_r * diff_r:
        print(0)
    elif d2 == diff_r * diff_r:
        print(1)
    else:
        print(2)