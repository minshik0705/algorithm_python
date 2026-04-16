import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon = [input().strip() for _ in range(N)]
name_to_num = {name: i + 1 for i, name in enumerate(pokemon)}

for _ in range(M):
    q = input().strip()
    if q.isdigit():
        print(pokemon[int(q) - 1])
    else:
        print(name_to_num[q])