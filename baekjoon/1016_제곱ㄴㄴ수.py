mi, ma = map(int,input().split())
squared = [i**2 for i in range(2,int(ma**0.5)+1)]
num = [1] * (ma-mi+1)
for i in squared:
  n = mi //i*i
  while(n < ma +1):
    if n - mi >= 0:
      num[n-mi] = 0
    n += i
print(sum(num))