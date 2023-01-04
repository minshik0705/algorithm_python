import sys
#sys.stdin=open("input.txt", 'r')
n=int(input())
#2차원 행렬 입력받기
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h, t, k=map(int, input().split())
    if t==0:
        #왼쪽으로 회전하기
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        #오른쪽으로 회전하기
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
            
#모래 시계의 합구하기
res=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    #좁혀들어가는 과정
    if i<n//2:
        s+=1
        e-=1
    #다시 넓어지는 과정
    else:
        s-=1
        e+=1
print(res)
