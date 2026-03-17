hour, minute = map(int, input().split())
time = int(input())
m = minute + time
while 1:
  if m >= 60:
    m -= 60
    hour += 1
  elif hour >= 24:
    hour -= 24
  else:
    print(hour,m)
    break