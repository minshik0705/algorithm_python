A = int(input())
B = int(input())
i = 10
j = 1
C = A*B
while i < 1001:
  K = A * (B % i)
  print(int(K/j))
  B = B - (B%i)
  i = i * 10
  j = j * 10
print(C)