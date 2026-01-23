M = int(input())
N = int(input())
decimals = []
for i in range(M,N+1):
  if i == 1:
    pass
  elif i == 2:
    decimals.append(i)
  else:
    for j in range(2,i):
      if i%j == 0:
        break
      elif j == i-1:
        decimals.append(i)
if decimals:
  print(sum(decimals))
  print(min(decimals))
else:
  print(-1)