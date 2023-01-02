import sys
#sys.stdin=open("input.txt", "rt")
T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))
    
'''
map(함수, 반복가능한 자료형(리스트, 튜플)) function, iterables라고 
map함수의 반환값은 map객체이기 때문에 해당 자료형을 list또는 tuple형으로 변환해야 한다.
리스트 또는 튜플의 각 요소에 접근할때 용이하게 사용된다.

      
