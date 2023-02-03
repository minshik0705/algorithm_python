'''
2.쇠막대기(스택)
'''
import sys
#sys.stdin=open("input.txt", "r")
s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':#레이저가 있다면
            cnt+=len(stack)#그동안 쌓은 (의 개수 만큼 count
        else:
            cnt+=1
print(cnt)
        
