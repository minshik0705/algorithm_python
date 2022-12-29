'''
#최소값 구하기

arr=[5, 3, 7, 9, 5, 2, 6]
arrMin=float('inf')
for i in range(len(arr)):   #for x in arr:
    if arr[i]<arrMin:
        arrMin=arr[i]
print(arrMin)
'''

'''
import sys
sys.stdin=open("input.txt","rt")
n=int(input())
a=list(map(int, input().split()))
b=list()
avg=sum(a)/n
print(avg)
for i in range(n):
    if avg>=a[i]:
        b[i]=avg-a[i]
    else:
        b[i]=a[i]-avg

min = b[0]
for j in range(n):
    if min > b[i]:
     b[i] = min   
'''
import sys
#sys.stdin=open("input.txt","rt")
n=int(input())
a=list(map(int, input().split()))
ave=(sum(a)/n) #round는 round_half_even방식을 택한다->.5는 짝수 쪽으로 
ave=ave+0.5
ave=int(ave)
min=2147000000
for idx, x in enumerate(a):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print(ave,res)



        
