import sys

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

month, day = map(int, sys.stdin.readline().strip().split(' '))
tot_days = 0
for i in range(month):
    tot_days += days[i]
tot_days += day - 1
print(week[tot_days % 7])