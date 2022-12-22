'''
문자열과 내장함수
'''
msg = "It is Time"
print(msg.upper()) #문자열을 대문자로 만드는 내장함수 upper
print(msg) #결과만 대문자이고 메모리에는 원본이 그대로임
print(msg.lower())
tmp = msg.upper() #tmp는 대문자화 된 변수
print(tmp)
print(tmp.find('T'))
#find는 index번호로 문자열을 찾는 함수
print(tmp.count('T'))
#count는 문자열을 세주는 함수
print(msg)
print(msg[:2])#2번 index전까지
print(msg[3:5])
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

#isupper함수-> 대문자인지 판별하는 함수 

for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

for x in msg:
    if x.islower():
        print(x, end = ' ')
print()

#공백 제거 함수
for x in msg:
    if x.isalpha():
        print(x, end= '')
print()

#ord ASCII를 출력하는 함수 
tmp='AZ'
for x in tmp:
    print(ord(x))

tmp='az'
for x in tmp:
    print(ord(x))

tmp=65
print(chr(tmp))
