'''
5.수들의 합
'''
#내풀이->틀림
'''
import sys
#sys.stdin=open("input.txt", "r")
N,M=map(int,input().split())
A=list(map(int, input().split(' ',N-1)))
i=0
j=1
tot=A[i]
cnt=0
for i in range(N):
    tot=A[i]  #->A[i]=M일경우를 해결 못함
    for j in range(i+1,N):
        tot+=A[j]
        if tot>M:
            tot=0
            break
        if tot==M:
            cnt+=1
        print(i, j,tot, cnt)
'''
import sys
#sys.stdin = open("input.txt", 'r')
n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)
