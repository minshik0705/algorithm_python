import sys

T = int(sys.stdin.readline().strip())
 
for i in range(T):
    floor = int(sys.stdin.readline().strip())
    room = int(sys.stdin.readline().strip())
    apt = [[0] * room for _ in range(floor + 1)]
    for k in range(floor + 1):
        for n in range(room):
            if k == 0:
                apt[k][n] = n + 1
            else:
                apt[k][n] = sum(apt[k - 1][:n + 1:])
    print(apt[floor][room - 1])
