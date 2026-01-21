dice = list(map(int, input().split()))
dice.sort()
a = dice[0]
b = dice[1]
c = dice[2]

if a==b and b==c:
  print(10000 + a * 1000)
elif a != b and b != c and a != c:
  print(c * 100)
else:
  print(1000 + b * 100)