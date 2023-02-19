import sys
#sys.stdin=open("input.txt", "rt")
def DFS(L, sum):
    if L==n and sum==f:#종료지점을 만나고 답을 찾으면
        for x in p:#순열을 저장한 리스트 출력
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:#중복을 방지하기
                ch[i]=1#사용하지 않는다
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))#sum업데이트하고 순회하기
                ch[i]=0

if __name__ == "__main__":
    n, f=map(int, input().split())
    p=[0]*n#순열을 만드는 리스트
    b=[1]*n#이항계수를 기록하는 리스트 
    ch=[0]*(n+1)
    for i in range(1, n):#1부터 n-1까지만 돌면 된다
        b[i]=b[i-1]*(n-i)//i#이항계수식
    DFS(0, 0)
