'''
람다 함수->내장 함수의 인자로 주로 사용하는 표현식 
'''
'''
def plus_one(x):
    return x+1

print(plus_one(1))

#x는 매개변수, plus_two는 할당받는 변수  
plus_two=lambda x: x+2
print(plus_two(1))
'''
#map(함수명, 자료)
#map(int(형 변환 내장함수), input, split)

def plus_one(x):
    return x+1

a=[1,2,3]
print(list(map(plus_one,a)))

#람다 표현식으로 쓰기
print(list(map(lambda x: x+1, a)))
      
