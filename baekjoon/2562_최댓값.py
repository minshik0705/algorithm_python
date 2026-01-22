A = []
max = 0
ind = 0
for i in range(9):
  a = int(input())
  A.append(a)
  if max < A[i]:
    max = A[i]
    ind = i+1
print(max)
print(ind)