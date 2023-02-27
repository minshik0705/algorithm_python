#시간 초과가 뜸
'''
N = int(stdin.readline())
card=list(range(1,N+1))
while len(card)>1:
    card.pop(0)
    card.append(card.pop(0))
print(card[0])
'''

#2번째 풀이->deq이용하기

from collections import deque

N=int(input())
card=deque([i for i in range(1,N+1)])
while len(card)>1:
    card.popleft()
    tmp=card.popleft()
    card.append(tmp)
print(card[0])

#3번째 풀이->output규칙 찾
input = int(input())
square = 2

while True:
    if (input == 1 or input == 2):
        print(input)
        break
    square *= 2
    if (square >= input):
        print((input - (square // 2)) * 2)
        break
