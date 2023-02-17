n=int(input())
fac=1
for i in range(1,n+1):
    fac=fac*i
if n==0:
    print(1)
else:
    print(fac)
