'''
점수 계산 
'''

import sys
#sys.stdin=open("input.txt", "rt")
n=int(input())
a=list(map(int, input().split()))
sum=0
cnt=0
for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0
print(sum)

'''
#내풀이
import sys
#sys.stdin=open("input.txt", "rt")
n=int(iput())
a=list(map(int, input().split(n-1)))
corr=0
score=0
for x in a:
    if x==1:
        corr+=1
        score+=corr
    else:
        corr=0
print(score)
'''   
