'''
import sys
#sys.stdin=open("input.txt", "rt")
n, k=map(int, input().split())
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
'''
#내 풀이 
n,k=map(int, input().split())
a=[]
for i in range (1,n+1):
    if n%i==0:
        a.append(i)
size=len(a)
if size>=k:
    print(a[k-1])
else:
    print(-1)

