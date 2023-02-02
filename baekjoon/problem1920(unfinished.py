#내 첫 풀이->시간 초과
'''
N=int(input())
a=list(map(int, input().split(' ', N-1)))
M=int(input())
b=list(map(int, input().split(' ', M-1)))
a.sort()
lt=0
rt=N-1
i=0
while lt<=rt:
    mid=(lt+rt)//2
    if b[i]>a[rt]:
        print(0)
        lt=0
        rt=N-1
        i+=1
    if b[i]==a[mid]:
         print(1)
        lt=0
        rt=N-1
        i+=1
    elif b[i]>a[mid]:
        lt=mid+1
    elif b[i]<a[mid]:
        rt=mid

'''


#1 i에대한 끝값을 지정하지 않음
#2 값들에 대한 갱신을 제데로 하지 않음

#chat gpt 풀이->출력 초과
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
        print(i)
'''

#내 코드 개선->틀림
'''
        
N = int(input())
a = list(map(int, input().split()))
a.sort()
M = int(input())
b = list(map(int, input().split()))

lt = 0
rt = N-1
i = 0
while i < M:
    while lt <= rt:
        mid = (lt + rt)//2
        if b[i] > a[rt]:
            print(0)
            break
        if b[i] == a[mid]:
            print(1)
            break
        elif b[i] > a[mid]:
            lt = mid + 1
        elif b[i] < a[mid]:
            rt = mid - 1
    lt = 0
    rt = N-1
    i+=1
'''




