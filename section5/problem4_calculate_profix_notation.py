'''
3.후위식 연산 
'''
import sys
#sys.stdin=open("input.txt", "r")
a=input()
stack=[]
for x in a:
    if x.isdecimal():#숫자인지 확인
        stack.append(int(x))#x자체는 문자열
    else:
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        elif x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
        elif x=='/'
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
print(stack[0])

