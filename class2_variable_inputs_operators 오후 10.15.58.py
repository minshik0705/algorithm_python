'''
변수입력과 연산자
'''
'''
a = input("숫자를 입력하세요: ")
print(a)
'''
'''
a, b = input("숫자를 입력하세요 : ").split()

print(a+b)#a,b가 문자형이라서 2,3입력시 5가 나오지 않음
print(type(a))
c = a+b #+는 문자 연결하는 연산자다 
print(type(c))
print(c)

a = int(a)
b = int(b)
print(a+b)

#map 함수 이용
a, b = map(int, input("숫자를 입력하세요: ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #몫 연산자
print(a%b) #나머지 연산자
print(a**b) #거듭제곱 연산자
'''

a = 4.3
b = 5
c = a + b
#c는 실수형이 된다-> 볌위가 넓은 자료형으로 변환된다.
print(type(c))
print(c)

#and or not == => <=


