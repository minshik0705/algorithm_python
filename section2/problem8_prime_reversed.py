'''
뒤집어진 소수
'''
import sys
#sys.stdin=open("input.txt","r")
def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    else:
        return True


n=int(input())
a=list(map(int, input().split()))
for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
        
#내풀이-> 미완성됨 0없애는 문제도 해결 못함
        
'''
import sys
#소수를 구하는 함수
def isPrime(x):
    value=1
    if x<=1:
        value=0
    for i in range(2,(x+1)//2): #수의 절반까지만 검색해도 소수인지 판별가능
        if x%i==0:
            value=0
    return value

#입력 받은 수를 역으로 출력하는 함수
def reverse(x):
    rev=list()
    count=0
    while x>0:
        rev.append(x%10)
        x=x//10
    return rev
    

N=int(input())
innum=list(map(int,input().split(' ',N-1)))

for i in innum:
    if isPrime(i)==1:
        print(reverse(i), end='')
'''
