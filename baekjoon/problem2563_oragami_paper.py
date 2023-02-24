from functools import reduce
S=[[0]*100 for i in range(100)]


def Fill(num1,num2):
    for i in range(num1, num1+10):
        for j in range(num2, num2+10):
            S[i][j]=1

N=int(input())
for _ in range(N):
    num1,num2=map(int, input().split())
    Fill(num1,num2)

flat_S = reduce(lambda x, y: x + y, S)
print(sum(flat_S))

