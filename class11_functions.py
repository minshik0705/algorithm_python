'''
함수 만들기

def add(a, b):
    c=a+b
    print(c)

add(3, 2)
add(5, 7)

'''
'''
def add(a,b):
    c=a+b
    d=a-b
    return c,d
#튜플이라는 자료구조로 반환한다.

p=add(3,2)
print(p)
'''

def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

a=[12,13,7,9,19]
for y in a:
    if isPrime(y):
        print(y,end=' ')
