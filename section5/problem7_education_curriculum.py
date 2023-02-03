import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
need=input()#필요한 수업의 순서
n=int(input())#계획된 수업코스의 수
for i in range(n):
    plan=input()#plan에 계획된 코수를 입력
    dq=deque(need)#dq에 need리스트를 deque로 저장
    for x in plan:
        if x in dq:#만약 x가 dq에 있고(필수과목 확인 여부)
            if x!=dq.popleft():#그 x가 dq의 첫번째 원소와 다르다면
                print("#%d NO" %(i+1))
                break
    else:#순서는 통과됨
        if len(dq)==0:#남아있지 않으면 plan에 모두 pop한 경우이므로
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

    
