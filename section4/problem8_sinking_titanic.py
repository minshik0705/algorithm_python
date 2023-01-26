'''
8.침몰하는 타이타닉
'''
'''
import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort()
p=deque(p)
cnt=0
while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.popleft()
        p.pop()
        cnt+=1
print(cnt)
'''
N,M=map(int,input().split())
pas=list(map(int,input().split(' ',N-1)))
pas.sort()
cnt=0
tot=0
tmp=0
for x in pas:
    tot=tot+x
    tmp+=1
    if tmp>2:
        cnt+=1
        tmp=0
        if tot>M:
            cnt+=1
            tot=x
            tmp=0
print(cnt)
