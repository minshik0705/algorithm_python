import sys
from collections import deque
#sys.stdin=open("input.txt", "rt")
n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate (list(map(int, input().split())))]
#(0,val), (1,val)....와 같은 튜플 형식으로 저장
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()#가장 앞의 자료를 cur에 저장
    if any(cur[1]<x[1] for x in Q):#만약 cur보다 위험도가 높은 사람이 있으면
        Q.append(cur)#cur를 목록의 뒤로 보내기
    else:#없으면
        cnt+=1#m번째 사람을 만날때까지 cnt 늘리기
        if cur[0]==m:
            print(cnt)
            break
        
    
    
