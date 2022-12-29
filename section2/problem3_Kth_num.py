'''
1부터 100사이의 자연수가 적힌 N장의 카드(같은 숫자의 카드가 여러장 있을 수 있다)
중 3장의 카드를 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 한다. 3장을 뽑을 수 있는
모든 경우를 고려할때 K번째로 큰 수를 출력하는 프로그램을 작성하세요
'''
'''
입력
10 3 -> N, K
13 15 34 23 45 65 33 11 26 42

출력: 143
'''

import sys
#sys.stdin=open("input.txt","rt")
n, k=map(int, input().split())
a=list(map(int, input().split()))
res=set() #중복을 제거하는 자료구조 set

#3개의 숫자를 뽑아야하기 때문에 3중 for문을 돌리는 것이다.
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res=list(res)#res list화
res.sort(reverse=True)
print(res[k-1])






#내 풀이 
''''
sys.stdin=open("input.txt", "rt")
N, K = map(int, input().split())
a=list(map(int,input().split()))
b=list()
for i in range(N):
    for j in range (N):
        b[i]=a[i+j] + a[i+1+j] + a[i+2+j]
b.sort()
print(b[k])
'''
#중복 제거법 모름, 3중 반복문, sort-> reverse가 오름차순인거 모름 ㄴㄴㄴ
