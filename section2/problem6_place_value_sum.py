'''
6.자리수의 합
'''
#내 풀이
import sys
n=int(input())
a=list(map(int, input().split(' ',n-1)))

def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum
max=-2147000000
for i in range(n):
    tot=digit_sum(a[i])
    if tot>max:
        max=tot
        res=a[i]
print(res)


#강의 풀이->리스트가 아닌 문자열로 접근 하기      
'''
n=int(input())
a=list(map(int, input().split()))
def digit_sum(x):
    sum=0
    for i in str(x):#문자 하나하나 접근하기 위한 반복문
        sum+= int(i)
    return sum

max=-2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)
'''
