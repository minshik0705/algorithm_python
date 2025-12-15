'''
2292번 벌집 문제
'''
N=int(input())
i=0
num=0  #하한 값을 기록하기 위한 변수
tmpnum=0  #상한 값을 기록하기 위한 변수
while True:
    num+=i
    i+=1
    tmpnum+=i
    maxlim=tmpnum*6 #상한
    minlim=num*6 #하한
    if N==1:#1입력시 1출력하고 종료
        print(1)
        break
    if N>minlim+1 and N<=maxlim+1:#벌집 이동 개수의 범위 
        print(i+1)
        break
    else:
        continue
