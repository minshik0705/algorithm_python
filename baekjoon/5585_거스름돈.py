import sys
input = sys.stdin.readline

pay = int(input().strip())
change = 1000 - pay
count = 0
while change:
    count += change // 500
    change %= 500
    count += change // 100
    change %= 100
    count += change // 50
    change %= 50
    count += change // 10
    change %= 10
    count += change // 5
    change %= 5
    count += change // 1
    change = 0
print(count)