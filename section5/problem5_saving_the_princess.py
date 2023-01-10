'''
4.공주 구하기(큐)
'''
import sys
from collections import deque
#sys.stdn=open("input.txt", "r")
n, k=map(int, input().split())
dq=list(range(1,n+1))
dq=deque(dq)#데크형으로 자료 구조 변경
while dq:
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()
