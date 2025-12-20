def fact(num, res):
    if num == 1:
        return res
    if num == 0:
        return 1
    else:
        res = res * num
        return(fact(num-1, res))

T=int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(fact(M,1)//(fact(N,1)*fact(M-N,1)))