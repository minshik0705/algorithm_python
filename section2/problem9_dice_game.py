'''
9.주사위 게임
'''
import sys
#sys.stdin=open("input.txt", "rt")
n=int(input())
res=0
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a, b, c=map(int,tmp)
    if a==b and b==c:
        money=10000+a*1000
    elif a==b or a==c:
        money=1000+a*100
    elif b==c:
        money=1000+b*100
    else:
        money=c*100
    if money>res:
        res=money
print(res)

#내풀이 
'''
N=int(input())
res=[0]*N
#리스트의 선언을 for문 안에서 하면 리스트가 계속 초기화된다.
money=0
for i in range(N):
    a,b,c=map(int, input().split())
    k=list()
    k.append(a)
    k.append(b)
    k.append(c)
    k.sort()
    if a==b and b==c:
        money=10000+a*1000
    elif a==b:
        money=1000+a*100
    elif b==c:
        money=1000+b*100
    else:
        money=100*a
    res[i]=money
res.sort(reverse=True)
print(res[0])
'''

