import sys
#sys.stdin-open("input.txt", ,"r")
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3): #회문의 길이가 5이기 때문에 3번만에 길이가 7인 리스트 검사가능
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            #회문 검사 5개는 2번만에 검사 됨
            #세로 검사시 서로 다른 숫자가 나오면
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt+=1
print(cnt)
                
