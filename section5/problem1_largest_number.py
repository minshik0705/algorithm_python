'''
1.가장 큰 수(스택)
'''

import sys
#sys.stdin=open("input.txt", "rt")
num, m=map(int, input().split())
#num을 스택 구현을 위해 리스트화 시키기
num=list(map(int, str(num)))#str형식으로 바꾸어서 각 하나의 숫자에 접근
stack=[]#->그냥 리스트형태의 자료구조
for x in num:
    while stack and m>0 and stack[-1]<x:
        #stack이 비어있지 않고 stack의 가장 최근 자료가 x보다 작을때
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
#스택을 스트링 형태로 변환
res=''.join(map(str, stack))
#낱개로 되어있는 자료를 다시 이어붙이기 위한 코드
#굳이 for문을 돌리지 않음
print(res)

#첫 풀이
'''
n, m=map(int, input().split())
a=list()
while n>1:
    a.append(n%10)
    n=n//10
a.sort(reverse=True)
k=len(a)-m

p=0
while p<k:
    print(a[p],end='')
    p+=1
->문제를 잘못 생각함
->순서를 유지 해야

#두번째 풀이
n, m=map(int, input().split())
a=list()
b=list()
while n>0:
    a.insert(0,n%10)
    n=n//10
print(a)

k=len(a)-m
i=0
while k>0 and len(b)<k:
    b.append(a[i])
    i+=1
    if a[i]>a[i-1]:
        b.remove(a[
print(b)
'''
