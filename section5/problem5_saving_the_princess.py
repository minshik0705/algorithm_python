'''
4.공주 구하기(큐)
'''

import sys
from collections import deque
#sys.stdn=open("input.txt", "r")
n, k=map(int, input().split())
dq=list(range(1,n+1))
dq=deque(dq)#데크형으로 자료 구조 변경
while dq:#dq가 비어있지 않은 동안
    for _ in range(k-1):#k-1번 반복
        cur=dq.popleft()#최근 cur는 dq의 가장 왼쪽 숫자를 저장
        dq.append(cur)#dq에 다시 cur를 저장
        #->k-1번 순회를 하는 코드
    dq.popleft()#세번째 왕자가 외치는 행위
    if len(dq)==1:#모든 왕자가 제외되고
        print(dq[0])
        dq.popleft()  

'''
n, k=map(int, input().split())
prince=list(range(1,n+1))#1부터 n까지
count=0
i=0
while prince:
    if count==3:
        prince.pop(prince[i])
        print(prince)
        count+=1
'''
