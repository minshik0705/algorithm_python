import sys
answerx = {}
answery = {}
for i in range(3):
    x, y = map(int, sys.stdin.readline().strip().split(' '))
    answerx[x] = answerx.get(x,0) + 1
    answery[y] = answery.get(y,0) + 1
for k, v in answerx.items():
    if v == 1:
        print(k, end = ' ')
for k, v in answery.items():
    if v == 1:
        print(k)