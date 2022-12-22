'''
리스트와 내장함수(2)
'''
'''
a=[23,12,36,53,19]
print(a[:3])
print(a[1:4])
print(len(a))
for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

#원소중 홀수 값만 출력
for x in a:
    if x%2==1:
        print(x, end=' ')
print()


#index번호와 x값을 출력 
for x in enumerate(a):
    print(x)
'''


b=(1,2,3,4,5) #소괄호는 리스트가 아닌 튜플
print(b[0])
#튜플은 원소값을 변경할 수 없다.
#b[0]=7
print(b[0])
#assignment=> 새로할당하는 것을 의미한다.

a=[23,12,36,53,19]
for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

#변수 x가 list a의 모든 원소를 접근
if all(50>x for x in a):
    print("YES")
else:
    print("NO")

#하나라도 참이면 실행된다.
if any(15>x for x in a):
    print("YES")
else:
    print("NO")
    
    
