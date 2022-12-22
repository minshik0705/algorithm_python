a=1 #대입 연산자 
A=2
c=3
print(a,A,c)

'''
변수명 정하기
1) 영문과 숫자, _로 이루어진다.
2) 대소문자를 구분한다.
3) 문자나, _로 시작한다.
4) 특수문자를 사용하면 안된다.(&, % 등)
5) 키워드를 사용하면 안된다.(if, for등)
'''

a, b, c = 3, 2, 1
print(a,b,c)
#기존 변수값 변경

#값 교환
a, b = 10, 20
print(a,b)
a,b = b,a
print(a,b)

#변수 타입
a = 12345
print(type(a))
a= 12.123456789123456789
#실수형은 8바이트까지만 저장이 가능하다
print(a)
print(type(a))
a= 'student' #""쌍 따음표도 가능
print(a)
print(type(a))


#출력방식
print("number")
a,b,c = 1,2,3
print(a, b, c)
print("number:", a,b,c)
print(a,b,c, sep = ', ')#seperate 각 변수 사이를 지정해주는 약어?
print(a,b,c, sep = '\n')
print(a)#기본적으로 '\n'이 있음
print(b)
print(c)
print(a, end = ' ')
print(b, end = ' ')
print(c)





