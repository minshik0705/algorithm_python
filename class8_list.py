'''
리스트와 내장함수(1)
'''
import random as r
#빈리스트 출력
a=[]
#print(a)
b=list()
#print(b)

a=[1,2,3,4,5]
#print(a)
#print(a[0])

b=list(range(1,11))
#print(b)

c=a+b #두리스트를 합치는 연산 
#print(c)
'''
print(a)
a.append(6)
print(a)

a.insert(3,7)

print(a)

print(a.pop())
a.pop(3)
print(a)

a.remove(4)#제거할 원소를 찾는 함수 index값이 아님 
print(a)

print(a.index(5))
'''

a=list(range(1,11))
print(a)
print(sum(a))
print(max(a))
print(min(a)) 
print(min(7,5))#인자값중에서 최소값을 찾음

r.shuffle(a)
print(a)
a.sort(reverse=True)
print(a)
a.sort()
print(a)
a.clear()
print(a)


