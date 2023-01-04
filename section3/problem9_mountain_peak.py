import sys
#sys.stdin=open("input.txt", 'r')
#x,y방향으로 탐색 경우의 수를 저장하는 리스트 
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
#2차원 행렬 입력받기
a=[list(map(int, input().split())) for _ in range(n)]

#0으로 가장자리 초기화하기
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)
#봉우리 개수 구하기
cnt=0
for i in range(1,n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
