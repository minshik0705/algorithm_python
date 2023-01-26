'''
랜선 자르기 결정 알고리즘
'''
import sys
#sys.stdin=open("input.txt", "r")
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt



k, n=map(int, input().split())
Line=[]
res=0
largest=0

for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)
lt=1
rt=largest
while lt<rt:
    mid=(lt+rt)//2
    print(lt , rt, mid)
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)

#내풀이
'''
def lineNum(mid):
    count=0
    for x in Line:
        count+=(x//mid)
    return  count

K,N=map(int, input().split())
Line=[]

for i in range(K):
    line=int(input())
    Line.append(line)
    
rt=sum(Line)//N
lt=1

while lt<rt:
    mid=(rt+lt)//2
    print(lt, rt, mid)
    if lineNum(mid)>=N:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)
        
'''
