N=int(input())
S=[]
for i in range(N):
    n=int(input())
    S.append(n)

S.sort()
for i in range(N):
    print(S[i])
