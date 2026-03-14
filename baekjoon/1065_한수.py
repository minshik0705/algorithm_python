import sys

input = sys.stdin.readline

N = int(input())
answer = 99
if N < 100:
    print(N)
else:
    for i in range(100, N + 1):
        string = str(i)
        length = len(string)
        check = []
        for ch in string:
            check.append(int(ch))

        if length % 2 == 1:
            if check[0] + check[-1] == 2 * check[length // 2]:
                answer += 1
        else:
            if check[0] + check[-1] == check[length // 2] + check[length // 2 - 1]:
                answer += 1
    print(answer)