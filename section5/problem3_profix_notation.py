'''
3.후위 표기식
'''
import sys
#sys.stdin=open("input.txt", "r")
a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal():#숫자면 바로 결과에 저장
        res+=x
    else:#연산자면 판단
        if x=='(':#우선순위가 가장 빠름
            stack.append(x)#stack에 저장
        elif x=='*' or x=='/':#다음 최우선 순위 '*', '/'
            while stack and (stack[-1]=='*' or stack[-1]=='/'):#stack이 비어있지 않고 '*','/'면
                res+=stack.pop()#결과에 가장 최신 연산자 저장
            stack.append(x)#다른 연산자는 그냥 stack에 저장
        elif x=='+' or x=='-':#덧셈과 뺄셈의 경우
            while stack and stack[-1]!='(':#최우선순위'('가 아니라면
                res+=stack.pop()#결과에 해당연산자 저장
            stack.append(x)#stack에 연산자 저장
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
