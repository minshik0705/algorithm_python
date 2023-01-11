'''
에라스토스테네스체(소수의 개수 구하기)
'''

import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
ch=[0]*(n+1)
cnt=0
for i in range(2,n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)

#에라스토스테네스의 체를 알기전 나의 풀이
#답은 맞지만 시간초과로 인해 틀림
'''
import sys
N=int(input())
#해당 인덱스 값을 수로 받고 소수면 1저장 반대는 0
prime=[0]*(N+1)

for idx, value in enumerate(prime):
    prime[idx]=1 #우선은 무조건 소수라고 인식한다
    if idx<=1: #인덱스 값이 2보다 작으면 소수가 아니다
            prime[idx]=0
    for j in range(2,idx): #만약 2부터 해당 인덱스 값까지 검색해고
        if idx%j==0: #나누어떨어지면
            prime[idx]=0 #0을 저장

print(sum(prime)) #소수의 개수 구하기
'''
