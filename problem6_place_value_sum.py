import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
'''
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
        return sum

'''
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
    
        
