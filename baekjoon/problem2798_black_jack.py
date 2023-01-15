'''
문제2798번 블랙잭 문제
'''
#내풀이

N,M=map(int, input().split())
a=list(map(int,input().split(' ', N-1)))
res=set()#집합 함수로 중복제거
for x in range(N):
    for y in range(N):
        for z in range(N): #모든 경우의 수를 탐색하되
            if x==y or y==z or x==z: #중복되는 경우는 제외한다
                continue
            res.add(a[x]+a[y]+a[z]) #합을 중복제거 set에 저장
res=list(res) #합 리스트화
res.sort() #오름차순 정렬->굳이 안해도 됨

##정답 탐색##
size=len(res) 
answer=0
for i in range(size):
    answer=res[i] #정답으로 무조건 초기화하고(res[i-1]이 없는 경우)
    if res[i]>M: #만약 주어진 수보다 크면 
        answer=res[i-1] #답을 이전 index값으로 갱신
        break
print(answer)

