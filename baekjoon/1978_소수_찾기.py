N=int(input())
a=list(map(int,input().split(' ',N-1)))

def prime_check(x):
    count=1
    if x<=1:
        return 0
    elif x==2:
        return 1
    for i in range(2,x):
        if x%i==0:
            count=0
    return count
    
b=list()
for i in range(N):
    b.append(prime_check(a[i]))

print(int(sum(b)))

