'''
조건문 if(분기, 중첩)
'''
'''
x = 7
if x==7:    #같다의 관계연산자 
    print("Lucky")  #들여쓰기 4칸
    print("ㅋㅋ")  #들여쓰기를 지키지 않으면 indent error가 발생함
    
x = 15
if x>=10:
    if x%2==1:
        print("10이상의 홀수")
x = 9
if x>0:
    if x<10:
        print("10보다 작은 자연수")

x=7
if x>0 and x<10:    #논리연산자 사용 
    print("10보다 작은 자연수")

x=7
if 0<x<10:
    print("10보다 작은 자연수")
    

x = 10
if x>0:
    print("양수")
else:   #양갈래로 나뉘는 분기문
    print("음수")

x = 50
if x>=90:
    print('A')
elif x>80:
    print('B')
elif x>=70:
    print('C')
elif x>60:
    print('D')
else:
    print('F')
#분기문은 하나의 문장구조라서 가장 위에서부터 조건의 참/거짓을 따진다.
'''
#전부 if문으로 만들면 각자 따로 따로 문장구조가 되기 때문에 ABCD로 출력이 된다.
    
