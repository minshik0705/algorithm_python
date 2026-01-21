import sys
for _ in range(3):
    yutnori = list(map(int, sys.stdin.readline().strip().split(' ')))
    yutnori.sort()
    if yutnori == [0, 0, 1, 1]:
        print('B')
    elif yutnori == [0, 1, 1, 1]:
        print('A')
    elif yutnori == [0, 0, 0, 1]:
        print('C')
    elif yutnori == [1, 1, 1, 1]:
        print('E')
    elif yutnori == [0, 0, 0, 0]:
        print('D')