A, B, C=map(int,input().split())

if B>=C: #같은 경우에도 손익 분기점을 넘을 수 없다
    print(-1)
else:
    profit=C-B #이윤의 크기에 따라 손익 분기점이 달리진다
    print(int(A//profit+1))
    
