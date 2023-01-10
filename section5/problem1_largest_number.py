'''
1.가장 큰 수(스택)
'''
import sys
#sys.stdin=open("input.txt", "rt")
num, m=map(int, input().split())
#num을 스택 구현을 위해 리스트화 시키기
num=list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
#스택을 스트링 형태로 변환
res=''.join(map(str, stack))
print(res)
