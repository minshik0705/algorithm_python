'''
n=int(input())
A=list(map(int, input().split(' ', n-1)))
m=int(input())
S=list(map(int, input().split(' ', m-1)))

A.sort()
lt=0
rt=n-1
pos=0
print(A[lt])
while lt<=rt:
    mid=(lt+rt)//2
    if S[pos]<A[lt]:
        print(0,S[pos], A[lt])
        pos+=1
    elif S[pos]<=A[mid]:
        rt=mid-1
    elif S[pos] >A[mid]:
        lt=mid+1
    elif lt==rt:
        print(1,pos)
        lt=0
        rt=n-1
        pos+=1
'''

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

#input
N = int(input())
a = list(map(int, input().split()))
a.sort()
M = int(input())
b = list(map(int, input().split()))

#searching
for i in b:
    if binary_search(a, i):
        print(1)
    else:
        print(0)


