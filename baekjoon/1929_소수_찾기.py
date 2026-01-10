M,N = map(int, input().split())
numbers = [0]* (N+1)
for i in range(2,N+1):
  j = 2 
  while i*j <= N:
    if numbers[i*j] == 0:
      numbers[i*j] = 1
    j += 1
for i in range(M,N+1):
  if numbers[i] == 0 and i != 1:
    print(i)